from __future__ import annotations

import json

from blockchain import Blockchain


def main() -> None:
    chain = Blockchain()
    chain.add_block({"msg": "genesis"})
    chain.add_block({"msg": "second"})
    print(json.dumps(chain.dump(), indent=2))


if __name__ == "__main__":
    main()
