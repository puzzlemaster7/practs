import os
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")

import tensorflow as tf
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


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

    x, y = make_moons(n_samples=1200, noise=0.25, random_state=42)
    x = x.astype(np.float32)
    y = y.astype(np.float32).reshape(-1, 1)

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train).astype(np.float32)
    x_test = scaler.transform(x_test).astype(np.float32)

    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(2,)),
            tf.keras.layers.Dense(32, activation="relu"),
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )
    model.compile(
        optimizer=tf.keras.optimizers.Adam(0.01),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )
    model.fit(x_train, y_train, epochs=40, batch_size=32, verbose=0)
    loss, acc = model.evaluate(x_test, y_test, verbose=0)

    print("TensorFlow version:", tf.__version__)
    print("Test loss:", float(loss))
    print("Test accuracy:", float(acc))

    # Decision boundary plot
    x0_min, x0_max = x_train[:, 0].min() - 1.0, x_train[:, 0].max() + 1.0
    x1_min, x1_max = x_train[:, 1].min() - 1.0, x_train[:, 1].max() + 1.0
    gx0, gx1 = np.meshgrid(np.linspace(x0_min, x0_max, 300), np.linspace(x1_min, x1_max, 300))
    grid = np.c_[gx0.ravel(), gx1.ravel()].astype(np.float32)

    probs = model.predict(grid, verbose=0).reshape(gx0.shape)
    preds = (probs >= 0.5).astype(np.int32)

    plt.figure(figsize=(7, 5))
    plt.contourf(gx0, gx1, preds, alpha=0.25, levels=[-0.5, 0.5, 1.5])
    plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train.reshape(-1), s=10, alpha=0.7, label="Train")
    plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test.reshape(-1), s=18, alpha=0.9, label="Test")
    plt.title("Binary Classification Decision Boundary")
    plt.xlabel("Feature 1 (scaled)")
    plt.ylabel("Feature 2 (scaled)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / "decision_boundary.png", dpi=160)
    plt.close()

    print("Saved: outputs/decision_boundary.png")


if __name__ == "__main__":
    main()
