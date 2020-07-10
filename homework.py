import datetime as dt

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount=amount
        self.date = dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment=comment 
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records=[]
    def add_record(self, record):
        self.records.append(record)
    def get_today_stats(self): 
        today_stats=0
        today=dt.datetime.now().date()
        for record in self.records:
            if record.date == today:
                today_stats = today_stats+record.amount
        return today_stats
    def get_week_stats(self): 
        week_stats=0
        today = dt.datetime.now().date()
        for record in self.records:
            if (today -  record.date).days <7 and (today -  record.date).days >=0:
                week_stats +=record.amount
        return week_stats
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        x=self.limit-self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {x} кКал'
        else:
            return 'Хватит есть!'
class CashCalculator(Calculator):
    USD_RATE=float(60) #Курс доллар США.
    EURO_RATE=float(70) #Курс Евро.   
    def get_today_cash_remained(self, currency, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type=currency
        cash_remained = self.limit - self.get_today_stats()
        if currency=='usd':
            cash_remained /= USD_RATE
            currency_type ='USD'
        elif currency_type=='eur':
            cash_remained /= EURO_RATE
            currency_type ='Euro'
        elif currency_type=='rub':
            cash_remained == 1.00
            currency_type ='руб'
        if cash_remained > 0:
            return 'На сегодня осталось {0:.2f} {1}'.format(cash_remained, currency_type)
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            return 'Денег нет, держись: твой долг - {0:.2f} {1}'.format(-cash_remained, currency_type)