import os
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import numpy as np

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")

import tensorflow as tf
import matplotlib.pyplot as plt
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


def load_digits_dataset():
    digits = load_digits()
    x = digits.images.astype(np.float32) / 16.0  # (n,8,8)
    y = digits.target.astype(np.int64)
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_state=42, stratify=y
    )
    return (x_train, y_train), (x_test, y_test)


def build_cnn():
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(8, 8, 1)),
            tf.keras.layers.Conv2D(16, 3, activation="relu"),
            tf.keras.layers.MaxPool2D(),
            tf.keras.layers.Conv2D(32, 3, activation="relu"),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )


def build_rnn():
    # Treat each row (8 values) as one timestep => sequence length 8
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(8, 8)),
            tf.keras.layers.GRU(64),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )


def run() -> None:
    tf.get_logger().setLevel("ERROR")
    tf.random.set_seed(42)

    (x_train, y_train), (x_test, y_test) = load_digits_dataset()

    # CNN
    cnn = build_cnn()
    cnn.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    cnn.fit(x_train[..., None], y_train, epochs=3, batch_size=64, verbose=0)
    cnn_loss, cnn_acc = cnn.evaluate(x_test[..., None], y_test, verbose=0)

    # RNN
    rnn = build_rnn()
    rnn.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    rnn.fit(x_train, y_train, epochs=3, batch_size=64, verbose=0)
    rnn_loss, rnn_acc = rnn.evaluate(x_test, y_test, verbose=0)

    print("TensorFlow version:", tf.__version__)
    print("CNN  test accuracy:", float(cnn_acc))
    print("RNN  test accuracy:", float(rnn_acc))


def main() -> None:
    buf = StringIO()
    with redirect_stdout(buf):
        run()
    save_terminal_outputs(buf.getvalue(), Path("outputs"))


if __name__ == "__main__":
    main()
