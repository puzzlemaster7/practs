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


def build_generator(latent_dim: int = 64) -> tf.keras.Model:
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(latent_dim,)),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(256, activation="relu"),
            tf.keras.layers.Dense(8 * 8, activation="tanh"),
            tf.keras.layers.Reshape((8, 8, 1)),
        ],
        name="generator",
    )


def build_discriminator() -> tf.keras.Model:
    return tf.keras.Sequential(
        [
            tf.keras.layers.Input(shape=(8, 8, 1)),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(256, activation="relu"),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(1),
        ],
        name="discriminator",
    )


def save_grid(images: np.ndarray, path: Path, n: int = 6) -> None:
    images = (images + 1.0) / 2.0  # tanh -> [0,1]
    plt.figure(figsize=(n, n))
    for i in range(n * n):
        plt.subplot(n, n, i + 1)
        plt.imshow(images[i, :, :, 0], cmap="gray")
        plt.axis("off")
    plt.tight_layout()
    plt.savefig(path, dpi=160)
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
    x_train = digits.images.astype(np.float32)  # (n,8,8) in [0..16]
    x_train = (x_train / 8.0) - 1.0  # map roughly to [-1,1]
    x_train = x_train[..., None]

    latent_dim = 64
    batch_size = 128
    steps = 400  # keeps runtime reasonable on CPU

    gen = build_generator(latent_dim)
    disc = build_discriminator()

    g_opt = tf.keras.optimizers.Adam(1e-4)
    d_opt = tf.keras.optimizers.Adam(1e-4)

    bce = tf.keras.losses.BinaryCrossentropy(from_logits=True)

    ds = tf.data.Dataset.from_tensor_slices(x_train).shuffle(10_000).batch(batch_size).repeat()
    it = iter(ds)

    @tf.function
    def train_step(real_images: tf.Tensor) -> tuple[tf.Tensor, tf.Tensor]:
        noise = tf.random.normal((tf.shape(real_images)[0], latent_dim))

        with tf.GradientTape() as d_tape:
            fake_images = gen(noise, training=True)
            real_logits = disc(real_images, training=True)
            fake_logits = disc(fake_images, training=True)
            d_loss = bce(tf.ones_like(real_logits), real_logits) + bce(
                tf.zeros_like(fake_logits), fake_logits
            )

        d_grads = d_tape.gradient(d_loss, disc.trainable_variables)
        d_opt.apply_gradients(zip(d_grads, disc.trainable_variables))

        noise = tf.random.normal((tf.shape(real_images)[0], latent_dim))
        with tf.GradientTape() as g_tape:
            fake_images = gen(noise, training=True)
            fake_logits = disc(fake_images, training=True)
            g_loss = bce(tf.ones_like(fake_logits), fake_logits)

        g_grads = g_tape.gradient(g_loss, gen.trainable_variables)
        g_opt.apply_gradients(zip(g_grads, gen.trainable_variables))
        return d_loss, g_loss

    for step in range(1, steps + 1):
        real = next(it)
        d_loss, g_loss = train_step(real)
        if step % 100 == 0:
            print(f"step={step:4d} d_loss={float(d_loss):.4f} g_loss={float(g_loss):.4f}")

    # Generate sample images
    noise = tf.random.normal((36, latent_dim))
    samples = gen(noise, training=False).numpy()
    out_path = out_dir / "generated_grid.png"
    save_grid(samples, out_path, n=6)

    print("TensorFlow version:", tf.__version__)
    print("Saved: outputs/generated_grid.png")


if __name__ == "__main__":
    main()
