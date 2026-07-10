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


def make_series(n: int = 1600) -> np.ndarray:
    rng = np.random.default_rng(42)
    t = np.arange(n, dtype=np.float32)
    trend = 0.02 * t
    season = 2.0 * np.sin(2 * np.pi * t / 50.0) + 0.8 * np.sin(2 * np.pi * t / 200.0)
    noise = rng.normal(0, 0.5, size=n).astype(np.float32)
    base = 50.0 + trend + season + noise
    return base.astype(np.float32)


def make_windows(series: np.ndarray, lookback: int = 30):
    x = []
    y = []
    for i in range(len(series) - lookback - 1):
        x.append(series[i : i + lookback])
        y.append(series[i + lookback])
    x = np.array(x, dtype=np.float32)[..., None]
    y = np.array(y, dtype=np.float32)
    return x, y


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

    series = make_series()
    lookback = 30
    x, y = make_windows(series, lookback)

    split = int(0.8 * len(x))
    x_train, y_train = x[:split], y[:split]
    x_test, y_test = x[split:], y[split:]

    model = tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(lookback, 1)),
            tf.keras.layers.LSTM(32),
            tf.keras.layers.Dense(1),
        ]
    )
    model.compile(optimizer=tf.keras.optimizers.Adam(1e-3), loss="mse")
    model.fit(x_train, y_train, epochs=8, batch_size=32, verbose=0)

    pred = model.predict(x_test, verbose=0).reshape(-1)

    plt.figure(figsize=(9, 4))
    plt.plot(y_test[:250], label="Actual")
    plt.plot(pred[:250], label="Predicted")
    plt.title("Sequence Prediction (LSTM): stock-price-like series")
    plt.xlabel("Time step (test)")
    plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()
    out_path = out_dir / "pred_vs_actual.png"
    plt.savefig(out_path, dpi=160)
    plt.close()

    mse = float(np.mean((y_test - pred) ** 2))
    print("TensorFlow version:", tf.__version__)
    print("Test MSE:", mse)
    print("Saved: outputs/pred_vs_actual.png")


if __name__ == "__main__":
    main()
