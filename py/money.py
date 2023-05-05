from __future__ import annotations


class Money:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount = amount
        self.currency = currency

    def times(self, multiplier: float) -> Money:
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor: float) -> Money:
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other: object) -> bool:
        return self.amount == other.amount and self.currency == other.currency

    def __str__(self) -> str:
        return f"{self.amount:0.2f} {self.currency}"

    def __repr__(self) -> str:
        return f"{self.amount:0.2f} {self.currency}"
