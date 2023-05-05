from money import Money


class Bank:
    def __init__(self) -> None:
        self.exchange_rates: dict[str, float] = {}

    def add_exchange_rate(self, currency_from: str, currency_to: str, rate: float):
        key = f"{currency_from}->{currency_to}"
        self.exchange_rates[key] = rate

    def convert(self, a_money: Money, a_currency: str) -> Money:
        if a_money.currency == a_currency:
            return a_money
        key = f"{a_money.currency}->{a_currency}"
        if key in self.exchange_rates:
            return Money(a_money.amount * self.exchange_rates[key], a_currency)
        raise Exception(key)
