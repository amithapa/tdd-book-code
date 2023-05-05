import functools
import operator
from money import Money


class Portfolio:
    def __init__(self) -> None:
        self.moneys: list[Money] = []
        self._eur_to_usd = 1.2

    def add(self, *moneys: Money):
        self.moneys.extend(moneys)

    def __convert(self, a_money: Money, a_currency: str) -> float:
        exchange_rates = {"EUR->USD": 1.2, "USD->KRW": 1100}

        if a_money.currency == a_currency:
            return a_money.amount
        else:
            key = f"{a_money.currency}->{a_currency}"
            return a_money.amount * exchange_rates[key]

    def evaluate(self, currency: str) -> Money:
        total = functools.reduce(
            operator.add,
            map(lambda m: self.__convert(m, currency), self.moneys),
            0,
        )
        return Money(total, currency)
