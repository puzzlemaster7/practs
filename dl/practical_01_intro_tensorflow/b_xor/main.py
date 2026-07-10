import os
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


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


def run() -> None:
    tf.random.set_seed(42)
    tf.get_logger().setLevel("ERROR")

    # XOR truth table
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], np.float32)
    y = np.array([[0], [1], [1], [0]], np.float32)

    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(2,)),
            tf.keras.layers.Dense(8, activation="tanh"),  # hidden layer makes XOR learnable
            tf.keras.layers.Dense(1, activation="sigmoid"),
        ]
    )

    model.compile(
        optimizer=tf.keras.optimizers.Adam(0.05),
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )

    model.fit(x, y, epochs=300, verbose=0)
    _, acc = model.evaluate(x, y, verbose=0)

    preds = model.predict(x, verbose=0)

    print("TensorFlow version:", tf.__version__)
    print("Training accuracy:", float(acc))
    print()
    print("x:\n", x.astype(int))
    print("y:", y.reshape(-1).astype(int))
    print("pred prob:", np.round(preds.reshape(-1), 4))
    print("pred 0/1:", (preds.reshape(-1) >= 0.5).astype(int))


def main() -> None:
    buf = StringIO()
    with redirect_stdout(buf):
        run()
    save_terminal_outputs(buf.getvalue(), Path("outputs"))


if __name__ == "__main__":
    main()
