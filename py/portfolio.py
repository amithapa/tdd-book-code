import functools
import operator
from money import Money
from bank import Bank


class Portfolio:
    def __init__(self) -> None:
        self.moneys: list[Money] = []
        self._eur_to_usd = 1.2

    def add(self, *moneys: Money):
        self.moneys.extend(moneys)

    def evaluate(self, bank: Bank, currency: str) -> Money:
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                total += bank.convert(m, currency).amount
            except Exception as ex:
                failures.append(ex)

        if len(failures) > 0:
            failure_message = ",".join(f.args[0] for f in failures)
            raise Exception(f"Missing exchange rate(s):[{failure_message}]")
        return Money(total, currency)
