import os
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")

import tensorflow as tf


def save_terminal_outputs(text: str, out_dir: Path) -> None:
    out_dir.mkdir(exist_ok=True)
    (out_dir / "terminal_output.txt").write_text(text, encoding="utf-8")
    lines = text.rstrip().splitlines() or [""]
    fig_w = 12
    fig_h = max(4, 0.22 * len(lines))
    plt.figure(figsize=(fig_w, fig_h), facecolor="#0c0c0c")
    plt.axis("off")
    plt.text(
        0.01,
        0.99,
        "\n".join(lines),
        va="top",
        ha="left",
        family="monospace",
        fontsize=10,
        color="#e6e6e6",
    )
    plt.tight_layout(pad=0.6)
    plt.savefig(out_dir / "terminal_output.png", dpi=170, facecolor="#0c0c0c")
    plt.close()


def draw_circle(mask: np.ndarray, cx: int, cy: int, r: int) -> None:
    h, w = mask.shape
    yy, xx = np.ogrid[:h, :w]
    circle = (xx - cx) ** 2 + (yy - cy) ** 2 <= r**2
    mask[circle] = 1.0


def draw_rect(mask: np.ndarray, x0: int, y0: int, x1: int, y1: int) -> None:
    mask[y0:y1, x0:x1] = 1.0


def make_synthetic_segmentation(
    n: int = 600, size: int = 64
) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(42)
    images = np.zeros((n, size, size, 1), dtype=np.float32)
    masks = np.zeros((n, size, size, 1), dtype=np.float32)

    for i in range(n):
        mask = np.zeros((size, size), dtype=np.float32)
        # 1-3 shapes
        for _ in range(rng.integers(1, 4)):
            if rng.random() < 0.5:
                cx, cy = int(rng.integers(10, size - 10)), int(rng.integers(10, size - 10))
                r = int(rng.integers(5, 12))
                draw_circle(mask, cx, cy, r)
            else:
                x0, y0 = int(rng.integers(0, size - 20)), int(rng.integers(0, size - 20))
                x1, y1 = x0 + int(rng.integers(8, 24)), y0 + int(rng.integers(8, 24))
                x1, y1 = min(x1, size), min(y1, size)
                draw_rect(mask, x0, y0, x1, y1)

        # Create an "image" as noisy mask (simulates a foreground object)
        img = mask + rng.normal(0, 0.25, size=(size, size)).astype(np.float32)
        img = np.clip(img, 0.0, 1.0)

        images[i, :, :, 0] = img
        masks[i, :, :, 0] = mask

    return images, masks


def build_unet(input_shape=(64, 64, 1)) -> tf.keras.Model:
    inputs = tf.keras.layers.Input(shape=input_shape)

    def conv(filters: int, x: tf.Tensor) -> tf.Tensor:
        x = tf.keras.layers.Conv2D(filters, 3, padding="same", activation="relu")(x)
        x = tf.keras.layers.Conv2D(filters, 3, padding="same", activation="relu")(x)
        return x

    c1 = conv(16, inputs)
    p1 = tf.keras.layers.MaxPool2D()(c1)

    c2 = conv(32, p1)
    p2 = tf.keras.layers.MaxPool2D()(c2)

    b = conv(64, p2)

    u2 = tf.keras.layers.UpSampling2D()(b)
    u2 = tf.keras.layers.Concatenate()([u2, c2])
    c3 = conv(32, u2)

    u1 = tf.keras.layers.UpSampling2D()(c3)
    u1 = tf.keras.layers.Concatenate()([u1, c1])
    c4 = conv(16, u1)

    outputs = tf.keras.layers.Conv2D(1, 1, activation="sigmoid")(c4)
    return tf.keras.Model(inputs, outputs)


def main() -> None:
    buf = StringIO()
    with redirect_stdout(buf):
        run()
    save_terminal_outputs(buf.getvalue(), Path("outputs"))


def run() -> None:
    tf.get_logger().setLevel("ERROR")
    tf.random.set_seed(42)

    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)

    x, y = make_synthetic_segmentation(n=700, size=64)
    x_train, y_train = x[:600], y[:600]
    x_test, y_test = x[600:], y[600:]

    model = build_unet((64, 64, 1))
    model.compile(optimizer=tf.keras.optimizers.Adam(1e-3), loss="binary_crossentropy")
    model.fit(x_train, y_train, epochs=6, batch_size=32, verbose=0)

    preds = model.predict(x_test[:6], verbose=0)

    # Visualize a few predictions
    plt.figure(figsize=(10, 6))
    for i in range(6):
        plt.subplot(3, 6, i + 1)
        plt.imshow(x_test[i, :, :, 0], cmap="gray")
        plt.axis("off")
        if i == 0:
            plt.title("Input")

        plt.subplot(3, 6, 6 + i + 1)
        plt.imshow(y_test[i, :, :, 0], cmap="gray")
        plt.axis("off")
        if i == 0:
            plt.title("Mask")

        plt.subplot(3, 6, 12 + i + 1)
        plt.imshow(preds[i, :, :, 0] >= 0.5, cmap="gray")
        plt.axis("off")
        if i == 0:
            plt.title("Pred")

    plt.suptitle("Segmentation: Synthetic Shapes (U-Net)")
    plt.tight_layout()
    out_path = out_dir / "sample_predictions.png"
    plt.savefig(out_path, dpi=160)
    plt.close()

    print("TensorFlow version:", tf.__version__)
    print("Saved: outputs/sample_predictions.png")


if __name__ == "__main__":
    main()
