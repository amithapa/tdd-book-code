import functools
import operator
from money import Money


class Portfolio:
    def __init__(self) -> None:
        self.moneys: list[Money] = []

    def add(self, *moneys: Money):
        self.moneys.extend(moneys)

    def evaluate(self, currency: str) -> Money:
        total = functools.reduce(operator.add, map(lambda m: m.amount, self.moneys), 0)
        return Money(total, currency)
