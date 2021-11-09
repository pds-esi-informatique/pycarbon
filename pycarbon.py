import datetime
class PyCarbon():
    def __init__(self):
        self.datetime_today = ''
    def __str__(self):
        if self.datetime_today and type(self.datetime_today) is datetime.datetime:
            return self.datetime_today.strftime("%Y-%m-%d, %H:%M:%S")
        return self.datetime_today
    def now(self):
        self.datetime_today = datetime.datetime.today()
        return self.datetime_today
    def add_days(self,days:int):
        self.datetime_today = self.datetime_today + datetime.timedelta(days=days)
        return self.datetime_today
    def add_day(self):
        self.datetime_today = self.datetime_today + datetime.timedelta(days=1)
        return self.datetime_today
    def sub_days(self,days:int):
        self.datetime_today = self.datetime_today - datetime.timedelta(days=days)
        return self.datetime_today
    def sub_day(self):
        self.datetime_today = self.datetime_today - datetime.timedelta(days=1)
        return self.datetime_today

