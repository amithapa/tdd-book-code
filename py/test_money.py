from __future__ import annotations
import unittest
import functools
import operator


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
        return f"{self.amount} {self.currency}"

    def __repr__(self) -> str:
        return f"{self.amount} {self.currency}"


class Portfolio:
    def __init__(self) -> None:
        self.moneys: list[Money] = []

    def add(self, *moneys: Money):
        self.moneys.extend(moneys)

    def evaluate(self, currency: str) -> Money:
        total = functools.reduce(operator.add, map(lambda m: m.amount, self.moneys), 0)
        return Money(total, currency)


class TestMoney(unittest.TestCase):
    def test_multiplication_in_dollars(self):
        five_dollars = Money(5, "USD")
        ten_dollars = Money(10, "USD")
        self.assertEqual(ten_dollars, five_dollars.times(2))

    def test_multiplication_in_euros(self):
        ten_euros = Money(10, "EUR")
        twenty_euros = Money(20, "EUR")
        self.assertEqual(twenty_euros, ten_euros.times(2))

    def test_division(self):
        original_money = Money(4002, "KRW")
        actual_money_after_division = original_money.divide(4)
        expected_money_after_division = Money(1000.5, "KRW")
        self.assertEqual(actual_money_after_division, expected_money_after_division)

    def test_addition(self):
        five_dollars = Money(5, "USD")
        ten_dollars = Money(10, "USD")
        fifteen_dollars = Money(15, "USD")

        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_dollars)
        self.assertEqual(fifteen_dollars, portfolio.evaluate("USD"))


if __name__ == "__main__":
    unittest.main()