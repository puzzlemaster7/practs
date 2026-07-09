from __future__ import annotations

import hashlib
import time


def mine(data: str, previous_hash: str, difficulty: int) -> tuple[int, str, float]:
    prefix = "0" * difficulty
    nonce = 0
    started = time.perf_counter()
    while True:
        payload = f"{data}|{previous_hash}|{nonce}".encode("utf-8")
        digest = hashlib.sha256(payload).hexdigest()
        if digest.startswith(prefix):
            elapsed = time.perf_counter() - started
            return nonce, digest, elapsed
        nonce += 1


def main() -> None:
    difficulty = 4
    nonce, digest, elapsed = mine(data="hello mining", previous_hash="0" * 64, difficulty=difficulty)
    print(f"difficulty={difficulty}")
    print(f"nonce={nonce}")
    print(f"hash={digest}")
    print(f"seconds={elapsed:.4f}")

if __name__ == "__main__":
    main()
