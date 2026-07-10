import os
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "3")
os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")

import tensorflow as tf


TOKENS = ["<pad>", "<bos>", "<eos>", "red", "green", "blue", "square", "circle"]
T2I = {t: i for i, t in enumerate(TOKENS)}
I2T = {i: t for t, i in T2I.items()}
PAD, BOS, EOS = T2I["<pad>"], T2I["<bos>"], T2I["<eos>"]


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


def render_shape(color: str, shape: str, size: int = 64) -> np.ndarray:
    img = np.zeros((size, size, 3), dtype=np.float32)
    color_map = {"red": (1.0, 0.1, 0.1), "green": (0.1, 1.0, 0.1), "blue": (0.1, 0.1, 1.0)}
    c = np.array(color_map[color], dtype=np.float32)

    yy, xx = np.mgrid[:size, :size]
    if shape == "square":
        mask = (xx > size * 0.25) & (xx < size * 0.75) & (yy > size * 0.25) & (yy < size * 0.75)
    else:
        cx, cy, r = size * 0.5, size * 0.5, size * 0.23
        mask = (xx - cx) ** 2 + (yy - cy) ** 2 <= r**2

    img[mask] = c
    # mild noise background
    img += np.random.default_rng(0).normal(0, 0.02, size=img.shape).astype(np.float32)
    img = np.clip(img, 0.0, 1.0)
    return img


def tokenize_caption(caption: str) -> list[int]:
    words = caption.strip().split()
    return [BOS, *(T2I[w] for w in words), EOS]


def pad_sequences(seqs: list[list[int]], pad_id: int) -> np.ndarray:
    max_len = max(len(s) for s in seqs)
    out = np.full((len(seqs), max_len), pad_id, dtype=np.int32)
    for i, s in enumerate(seqs):
        out[i, : len(s)] = np.array(s, dtype=np.int32)
    return out


def build_model(vocab_size: int, embed_dim: int = 32, rnn_units: int = 64) -> tf.keras.Model:
    image_in = tf.keras.layers.Input(shape=(64, 64, 3), name="image")
    seq_in = tf.keras.layers.Input(shape=(None,), dtype=tf.int32, name="seq")

    # CNN encoder -> feature vector
    x = tf.keras.layers.Conv2D(16, 3, activation="relu", padding="same")(image_in)
    x = tf.keras.layers.MaxPool2D()(x)
    x = tf.keras.layers.Conv2D(32, 3, activation="relu", padding="same")(x)
    x = tf.keras.layers.MaxPool2D()(x)
    x = tf.keras.layers.Conv2D(64, 3, activation="relu", padding="same")(x)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    img_feat = tf.keras.layers.Dense(rnn_units, activation="relu")(x)

    # Token embedding
    emb = tf.keras.layers.Embedding(vocab_size, embed_dim, mask_zero=True)(seq_in)

    # Condition LSTM on image feature by using it as initial state
    h0 = img_feat
    c0 = tf.keras.layers.Dense(rnn_units, activation="tanh")(img_feat)
    lstm_out = tf.keras.layers.LSTM(rnn_units, return_sequences=True)(emb, initial_state=[h0, c0])
    logits = tf.keras.layers.Dense(vocab_size)(lstm_out)

    return tf.keras.Model(inputs={"image": image_in, "seq": seq_in}, outputs=logits)


def greedy_decode(model: tf.keras.Model, image: np.ndarray, max_len: int = 6) -> str:
    seq = [BOS]
    for _ in range(max_len):
        seq_arr = np.array(seq, dtype=np.int32)[None, :]
        logits = model.predict({"image": image[None, ...], "seq": seq_arr}, verbose=0)
        next_id = int(np.argmax(logits[0, -1]))
        seq.append(next_id)
        if next_id == EOS:
            break
    words = []
    for tid in seq[1:]:
        if tid in (EOS, PAD):
            break
        words.append(I2T[tid])
    return " ".join(words)


def main() -> None:
    buf = StringIO()
    with redirect_stdout(buf):
        run()
    save_terminal_outputs(buf.getvalue(), Path("outputs"))


def run() -> None:
    tf.get_logger().setLevel("ERROR")
    tf.random.set_seed(42)
    np.random.seed(42)

    out_dir = Path("outputs")
    out_dir.mkdir(parents=True, exist_ok=True)

    # Tiny dataset
    items: list[tuple[np.ndarray, str]] = [
        (render_shape("red", "square"), "red square"),
        (render_shape("green", "square"), "green square"),
        (render_shape("blue", "square"), "blue square"),
        (render_shape("red", "circle"), "red circle"),
        (render_shape("green", "circle"), "green circle"),
        (render_shape("blue", "circle"), "blue circle"),
    ]

    images = np.stack([im for im, _ in items], axis=0).astype(np.float32)
    seqs = [tokenize_caption(cap) for _, cap in items]
    seq_padded = pad_sequences(seqs, PAD)

    # Teacher forcing: input is caption[:-1], target is caption[1:]
    x_seq = seq_padded[:, :-1]
    y_seq = seq_padded[:, 1:]

    model = build_model(vocab_size=len(TOKENS))
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(optimizer=tf.keras.optimizers.Adam(1e-3), loss=loss_fn)

    model.fit({"image": images, "seq": x_seq}, y_seq, epochs=120, verbose=0)

    # Test on a sample image
    test_img = render_shape("red", "circle")
    plt.figure(figsize=(3, 3))
    plt.imshow(test_img)
    plt.axis("off")
    sample_path = out_dir / "sample_image.png"
    plt.tight_layout()
    plt.savefig(sample_path, dpi=160)
    plt.close()

    pred = greedy_decode(model, test_img)

    print("TensorFlow version:", tf.__version__)
    print("Predicted caption:", pred)
    print("Saved: outputs/sample_image.png")


if __name__ == "__main__":
    main()
