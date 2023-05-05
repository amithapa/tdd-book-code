from __future__ import annotations
import unittest


class Dollar:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def times(self, multiplier: float) -> Dollar:
        return Dollar(self.amount * multiplier)


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)


if __name__ == "__main__":
    unittest.main()
