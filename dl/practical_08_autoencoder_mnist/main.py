import os
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")

import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split


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

    digits = load_digits()
    x = digits.data.astype(np.float32) / 16.0  # 64 dims
    x_train, x_test = train_test_split(x, test_size=0.2, random_state=42)

    inp = tf.keras.layers.Input(shape=(64,))
    enc = tf.keras.layers.Dense(128, activation="relu")(inp)
    enc = tf.keras.layers.Dense(32, activation="relu")(enc)
    dec = tf.keras.layers.Dense(128, activation="relu")(enc)
    out = tf.keras.layers.Dense(64, activation="sigmoid")(dec)
    autoencoder = tf.keras.Model(inp, out)
    autoencoder.compile(optimizer="adam", loss="mse")

    autoencoder.fit(x_train, x_train, epochs=5, batch_size=256, verbose=0, validation_split=0.1)

    recon = autoencoder.predict(x_test[:12], verbose=0).reshape(-1, 8, 8)

    plt.figure(figsize=(10, 4))
    for i in range(12):
        plt.subplot(2, 12, i + 1)
        plt.imshow(x_test[i].reshape(8, 8), cmap="gray")
        plt.axis("off")
        plt.subplot(2, 12, 12 + i + 1)
        plt.imshow(recon[i], cmap="gray")
        plt.axis("off")
    plt.suptitle("Digits Autoencoder (Top: original, Bottom: reconstruction)")
    plt.tight_layout()
    out_path = out_dir / "digits_recon.png"
    plt.savefig(out_path, dpi=160)
    plt.close()

    print("TensorFlow version:", tf.__version__)
    print("Saved: outputs/digits_recon.png")


if __name__ == "__main__":
    main()
