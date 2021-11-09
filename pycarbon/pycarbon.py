import datetime
class PyCarbon():
    def __init__(self):
        self.datetime_today = None
    def __str__(self):
        if self.datetime_today and type(self.datetime_today) is datetime.datetime:
            return self.datetime_today.strftime("%Y-%m-%d, %H:%M:%S")
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
    def to_date_time_string(self):
        return self.datetime_today.strftime("%Y-%m-%d, %H:%M:%S")
    def to_date_string(self):
        return self.datetime_today.strftime("%Y-%m-%d")
    def to_atom_string(self):
        return self.datetime_today.astimezone().replace(tzinfo=datetime.timezone.utc).isoformat()
    def to_iso8601_string(self):
        return self.datetime_today.astimezone().replace(microsecond=0).isoformat()
