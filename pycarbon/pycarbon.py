import datetime
import calendar


class PyCarbon:
    def __init__(self):
        self.datetime_today = None

    def __str__(self):
        if self.datetime_today and type(self.datetime_today) is datetime.datetime:
            return self.datetime_today.strftime("%Y-%m-%d, %H:%M:%S")

    def __repr__(self):
        if self.datetime_today and type(self.datetime_today) is datetime.datetime:
            return self.datetime_today.strftime("%Y-%m-%d, %H:%M:%S")

    @staticmethod
    def _positive_parameter_number(number):
        return abs(number)

    @staticmethod
    def _calculate_months(datetime_today, months: int):
        """
        https://stackoverflow.com/questions/4130922/how-to-increment-datetime-by-custom-months-in-python-without-using-library/23506665
        """
        month = datetime_today.month - 1 + months
        year = datetime_today.year + month // 12
        month = month % 12 + 1
        day = min(datetime_today.day, calendar.monthrange(year, month)[1])
        return datetime_today.replace(year=year, month=month, day=day)

    @staticmethod
    def _calculate_days(datetime_today, days: int):
        return datetime_today + datetime.timedelta(days=days)

    def now(self):
        self.datetime_today = datetime.datetime.today()
        return self

    def add_day(self):
        self.datetime_today = self._calculate_days(self.datetime_today, 1)
        return self

    def add_days(self, days: int):
        days = self._positive_parameter_number(days)
        self.datetime_today = self._calculate_days(self.datetime_today, days)
        return self

    def sub_day(self):
        self.datetime_today = self._calculate_days(self.datetime_today, -1)
        return self

    def sub_days(self, days: int):
        days = self._positive_parameter_number(days)
        self.datetime_today = self._calculate_days(self.datetime_today, -days)
        return self

    def add_month(self):
        self.datetime_today = self._calculate_months(self.datetime_today, 1)
        return self

    def add_months(self, months: int):
        months = self._positive_parameter_number(months)
        self.datetime_today = self._calculate_months(self.datetime_today, months)
        return self

    def sub_month(self):
        self.datetime_today = self._calculate_months(self.datetime_today, -1)
        return self

    def sub_months(self, months: int):
        months = self._positive_parameter_number(months)
        self.datetime_today = self._calculate_months(self.datetime_today, -months)
        return self

    def first_of_month(self):
        self.datetime_today = self.datetime_today.replace(day=1)
        return self

    def start_of_month(self):
        self.datetime_today = self.datetime_today.replace(day=1, hour=0, minute=0, second=0)
        return self

    def to_date_time_string(self):
        return self.datetime_today.strftime("%Y-%m-%d, %H:%M:%S")

    def to_date_string(self):
        return self.datetime_today.strftime("%Y-%m-%d")

    def to_atom_string(self):
        return self.datetime_today.astimezone().replace(tzinfo=datetime.timezone.utc).isoformat()

    def to_iso8601_string(self):
        return self.datetime_today.astimezone().replace(microsecond=0).isoformat()
