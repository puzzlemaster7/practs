from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone


class Blockchain:
    def __init__(self) -> None:
        self._chain: list[dict] = []

    def add_block(self, data: dict) -> None:
        previous_hash = self._chain[-1]["hash"] if self._chain else "0" * 64
        block = {
            "index": len(self._chain),
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "data": data,
            "previous_hash": previous_hash,
        }

        block_bytes = json.dumps(block, sort_keys=True, separators=(",", ":")).encode("utf-8")
        block["hash"] = hashlib.sha256(block_bytes).hexdigest()
        self._chain.append(block)

    def dump(self) -> list[dict]:
        return list(self._chain)
