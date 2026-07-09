from __future__ import annotations

import base64

import secrets
from dataclasses import dataclass


def _egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    g, x1, y1 = _egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def _modinv(a: int, m: int) -> int:
    g, x, _ = _egcd(a, m)
    if g != 1:
        raise ValueError("modular inverse does not exist")
    return x % m


def _is_probable_prime(n: int, rounds: int = 12) -> bool:
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    if n in small_primes:
        return True
    if any(n % p == 0 for p in small_primes):
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(rounds):
        a = secrets.randbelow(n - 3) + 2  # [2, n-2]
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _r in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def _random_odd_int(bits: int) -> int:
    x = secrets.randbits(bits)
    x |= 1
    x |= 1 << (bits - 1)
    return x


def _generate_prime(bits: int) -> int:
    while True:
        candidate = _random_odd_int(bits)
        if _is_probable_prime(candidate):
            return candidate


@dataclass(frozen=True)
class RsaPublicKey:
    n: int
    e: int


@dataclass(frozen=True)
class RsaPrivateKey:
    n: int
    d: int


def generate_rsa_keypair(bits: int = 512, e: int = 65537) -> tuple[RsaPublicKey, RsaPrivateKey]:
    # Educational RSA for labs (NOT production secure).
    half = bits // 2
    while True:
        p = _generate_prime(half)
        q = _generate_prime(half)
        if p == q:
            continue
        n = p * q
        phi = (p - 1) * (q - 1)
        if phi % e != 0:
            d = _modinv(e, phi)
            return RsaPublicKey(n=n, e=e), RsaPrivateKey(n=n, d=d)


def rsa_encrypt(pub: RsaPublicKey, plaintext: bytes) -> bytes:
    m = int.from_bytes(plaintext, byteorder="big")
    if m >= pub.n:
        raise ValueError("Message too large for this key size.")
    c = pow(m, pub.e, pub.n)
    k = (pub.n.bit_length() + 7) // 8
    return c.to_bytes(k, byteorder="big")


def rsa_decrypt(priv: RsaPrivateKey, ciphertext: bytes) -> bytes:
    c = int.from_bytes(ciphertext, byteorder="big")
    m = pow(c, priv.d, priv.n)
    k = (priv.n.bit_length() + 7) // 8
    raw = m.to_bytes(k, byteorder="big")
    return raw.lstrip(b"\x00")


def main() -> None:
    sender = "alice"
    receiver = "bob"
    message = "Hello Bob, this is Alice."

    pub, priv = generate_rsa_keypair(bits=512)
    ciphertext = rsa_encrypt(pub, message.encode("utf-8"))
    plaintext = rsa_decrypt(priv, ciphertext).decode("utf-8")

    print("=== Secure Messaging (RSA) Demo ===")
    print(f"sender={sender}")
    print(f"receiver={receiver}")
    print(f"message={message}")
    print()
    print("receiver_public_key:")
    print(f"n_bits={pub.n.bit_length()}")
    print(f"e={pub.e}")
    print()
    print("ciphertext_base64:")
    print(base64.b64encode(ciphertext).decode("ascii"))
    print()
    print("decrypted_message:")
    print(plaintext)


if __name__ == "__main__":
    main()
