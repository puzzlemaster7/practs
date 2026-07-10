import os
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")

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
    tf.get_logger().setLevel("ERROR")

    print("TensorFlow version:", tf.__version__)
    print()

    # 1) Tensors (shapes + dtypes)
    scalar = tf.constant(3.14, tf.float32)
    vector = tf.constant([1, 2, 3], tf.int32)
    matrix = tf.constant([[1.0, 2.0], [3.0, 4.0]], tf.float64)
    tensor3d = tf.ones((2, 3, 4), tf.float32)

    print("scalar:", scalar)
    print("vector:", vector)
    print("matrix:\n", matrix)
    print("tensor3d shape:", tensor3d.shape)
    print()

    # 2) Basic ops
    a = tf.constant([1.0, 2.0, 3.0])
    b = tf.constant([0.5, 0.25, 0.125])
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)
    print()

    # 3) Reshape + slice + index
    x = tf.reshape(tf.range(12), (3, 4))
    print("x:\n", x.numpy())
    print("x[1] (row 1):", x[1].numpy())
    print("x[2,3] (element):", x[2, 3].numpy())
    print("x[0:2,1:3] (slice):\n", x[0:2, 1:3].numpy())
    print()

    # 4) Matrix multiplication
    m1 = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    m2 = tf.constant([[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]])
    print("m1 @ m2:\n", tf.matmul(m1, m2).numpy())
    print()

    # 5) Eigenvalues + eigenvectors (symmetric matrix)
    sym = tf.constant([[4.0, 1.0], [1.0, 3.0]], dtype=tf.float32)
    eigenvalues, eigenvectors = tf.linalg.eigh(sym)
    print("Symmetric matrix:\n", sym.numpy())
    print("Eigenvalues:", eigenvalues.numpy())
    print("Eigenvectors (columns):\n", eigenvectors.numpy())


def main() -> None:
    buf = StringIO()
    with redirect_stdout(buf):
        run()
    save_terminal_outputs(buf.getvalue(), Path("outputs"))


if __name__ == "__main__":
    main()
