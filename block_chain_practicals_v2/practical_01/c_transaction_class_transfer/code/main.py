from __future__ import annotations

from transaction import Transaction


def main() -> None:
    balances = {"alice": 1000.0, "bob": 200.0}
    tx = Transaction(sender="alice", receiver="bob", amount=50.0)
    print("Before:", balances)
    tx.transfer(balances)
    print("After:", balances)


if __name__ == "__main__":
    main()
