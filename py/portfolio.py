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
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                total += self.__convert(m, currency)
            except KeyError as ke:
                failures.append(ke)

        if len(failures) > 0:
            failure_message = ",".join(f.args[0] for f in failures)
            raise Exception(f"Missing exchange rate(s):[{failure_message}]")
        return Money(total, currency)
