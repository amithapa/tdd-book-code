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
        if a_money.currency == a_currency:
            return a_money.amount
        else:
            return a_money.amount * self._eur_to_usd

    def evaluate(self, currency: str) -> Money:
        total = functools.reduce(
            operator.add,
            map(lambda m: self.__convert(m, currency), self.moneys),
            0,
        )
        return Money(total, currency)
