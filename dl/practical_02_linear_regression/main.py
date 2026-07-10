import os
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")

import tensorflow as tf


def load_csv(csv_path: Path) -> tuple[np.ndarray, np.ndarray]:
    data = np.genfromtxt(csv_path, delimiter=",", skip_header=1, dtype=np.float32)
    sqft = data[:, 0:1]
    price = data[:, 1:2]
    return sqft, price


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

    out_dir = Path("outputs")
    out_dir.mkdir(exist_ok=True)

    x, y = load_csv(Path("data") / "housing_toy.csv")

    # Model: y = w*x + b
    model = tf.keras.Sequential(
        [tf.keras.layers.Input(shape=(1,)), tf.keras.layers.Dense(1)]
    )

    model.compile(optimizer=tf.keras.optimizers.Adam(0.05), loss="mse")
    hist = model.fit(x, y, epochs=200, verbose=0).history["loss"]

    # 1) Loss curve
    plt.figure(figsize=(7, 4))
    plt.plot(hist)
    plt.title("Training Loss (MSE)")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.tight_layout()
    plt.savefig(out_dir / "loss_curve.png", dpi=160)
    plt.close()

    # Learned parameters
    w, b = model.layers[0].get_weights()
    print("TensorFlow version:", tf.__version__)
    print("Learned weight (w):", float(w.squeeze()))
    print("Learned bias (b):", float(b.squeeze()))
    print("Final training loss:", float(hist[-1]))
    print()

    # 2) Data + best-fit line
    x_line = np.linspace(x.min(), x.max(), 200, np.float32).reshape(-1, 1)
    y_line = model.predict(x_line, verbose=0).reshape(-1)

    plt.figure(figsize=(7, 4))
    plt.scatter(x.reshape(-1), y.reshape(-1), s=18, alpha=0.7, label="Data")
    plt.plot(x_line.reshape(-1), y_line, "r", linewidth=2, label="Learned line")
    plt.title("Linear Regression: Price vs Square Footage")
    plt.xlabel("Square Footage")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_dir / "fit_line.png", dpi=160)
    plt.close()

    # 3) Predictions
    new_sqft = np.array([[800.0], [1500.0], [2500.0], [3200.0]], np.float32)
    preds = model.predict(new_sqft, verbose=0).reshape(-1)
    print("Predictions:")
    for s, p in zip(new_sqft.reshape(-1), preds):
        print(f"  sqft={s:7.0f} -> price={p:,.2f}")
    print()
    print("Saved plots to: outputs/")


def main() -> None:
    buf = StringIO()
    with redirect_stdout(buf):
        run()
    save_terminal_outputs(buf.getvalue(), Path("outputs"))


if __name__ == "__main__":
    main()
