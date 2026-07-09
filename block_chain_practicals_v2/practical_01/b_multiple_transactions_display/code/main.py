from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class Transaction:
    sender: str
    receiver: str
    amount: float
    timestamp_utc: str


def _format_table(rows: list[list[str]], headers: list[str]) -> str:
    columns = list(zip(*([headers] + rows))) if rows else [headers]
    widths = [max(len(str(cell)) for cell in col) for col in columns]

    def fmt_row(row: list[str]) -> str:
        return " | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row))

    sep = "-+-".join("-" * w for w in widths)
    out = [fmt_row(headers), sep]
    out.extend(fmt_row(r) for r in rows)
    return "\n".join(out)


def main() -> None:
    # Self-contained demo (no interactive input) so it runs the same everywhere.
    now = datetime.now(timezone.utc).isoformat()
    txs = [
        Transaction("alice", "bob", 50.0, now),
        Transaction("bob", "carol", 10.5, now),
        Transaction("alice", "dave", 5.25, now),
    ]

    headers = ["#", "sender", "receiver", "amount", "timestamp_utc"]
    rows = [
        [str(i + 1), tx.sender, tx.receiver, f"{tx.amount:.2f}", tx.timestamp_utc]
        for i, tx in enumerate(txs)
    ]

    print("=== Multiple Transactions (Organized Display) ===")
    print(_format_table(rows, headers))


if __name__ == "__main__":
    main()
