import datetime as dt


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.date = (
            dt.date.today()
            if date is None
            else dt.datetime.strptime(date, '%d.%m.%Y').date()
        )
        self.comment = comment


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_stats = 0
        today = dt.date.today()
        today_stats = sum([record.amount
                           for record in self.records
                           if record.date == today])
        return today_stats

    def today_remained(self):
        remained = self.limit - self.get_today_stats()
        return remained

    def get_week_stats(self):
        week_stats = 0
        today = dt.date.today()
        week_stats = sum([record.amount
                          for record in self.records
                          if 0 <= (today-record.date).days < 7])
        return week_stats


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        if self.today_remained() > 0:
            return(
                f"Сегодня можно съесть что-нибудь ещё, но "
                f"с общей калорийностью не более {self.today_remained()} кКал"
            )
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = float(60)
    EURO_RATE = float(70)
    RUB_RATE = float(1)

    def get_today_cash_remained(self, currency):
        currencies = {
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE),
            'rub': ('руб', self.RUB_RATE),
        }
        value_currency = (str(abs(round(
            self.today_remained()
            / currencies[currency][1], 2)))
            + ' '
            + str(currencies[currency][0]))
        if not self.today_remained():
            return 'Денег нет, держись'
        elif self.today_remained() > 0:
            return(f"На сегодня осталось {value_currency}")
        elif self.today_remained() < 0:
            return(f"Денег нет, держись: твой долг - {value_currency}")
