import unittest

from money import Money
from portfolio import Portfolio


class TestMoney(unittest.TestCase):
    def test_multiplication(self):
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

    def test_addition_of_dollars_and_euros(self):
        five_dollars = Money(5, "USD")
        ten_euros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_euros)
        expected_value = Money(17, "USD")
        actual_value = portfolio.evaluate("USD")
        self.assertEqual(expected_value, actual_value)

    def test_addition_of_dollars_and_wons(self):
        one_dollar = Money(1, "USD")
        eleven_hundred_won = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar, eleven_hundred_won)
        expected_value = Money(2200, "KRW")
        actual_value = portfolio.evaluate("KRW")

        self.assertEqual(actual_value, expected_value)


if __name__ == "__main__":
    unittest.main()
