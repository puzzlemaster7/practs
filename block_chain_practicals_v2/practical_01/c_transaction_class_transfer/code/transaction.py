from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Transaction:
    sender: str
    receiver: str
    amount: float

    def transfer(self, balances: dict[str, float]) -> None:
        if self.amount <= 0:
            raise ValueError("Amount must be > 0.")
        if self.sender not in balances:
            raise KeyError(f"Unknown sender: {self.sender}")
        if self.receiver not in balances:
            raise KeyError(f"Unknown receiver: {self.receiver}")
        if balances[self.sender] < self.amount:
            raise ValueError("Insufficient funds.")

        balances[self.sender] -= self.amount
        balances[self.receiver] += self.amount
