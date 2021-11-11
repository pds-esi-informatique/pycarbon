import datetime
import calendar
import re
import pytz

MONTHS = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06", "july": "07",
          "august": "08", "september": "09", "october": "10", "november": "11", "december": "12"}


class PyCarbon:
    def __init__(self, date: str = None):
        self.datetime_today = datetime.datetime.today()
        if date:
            remove_space_in_date = date.replace(" ", "")
            if 'firstdayof' in remove_space_in_date.replace(" ", "").lower():
                year = "".join(filter(str.isdigit, remove_space_in_date))
                month_search = re.sub(r"\d+", "", remove_space_in_date.replace('firstdayof', '').lower())
                if month_search in MONTHS.keys():
                    self.datetime_today = self.datetime_today.replace(day=1, month=int(MONTHS[month_search]))
                if year:
                    self.datetime_today = self.datetime_today.replace(day=1, year=int(year),
                                                                      month=int(MONTHS[month_search]))

    def __str__(self):
        return self._date_representation

    def __repr__(self):
        return self._date_representation

    @property
    def _date_representation(self):
        if self.datetime_today and type(self.datetime_today) is datetime.datetime:
            if self.datetime_today.tzname():
                return self.datetime_today.strftime("%Y-%m-%d, %H:%M:%S ") + str(self.datetime_today.tzinfo)
            else:
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

    @staticmethod
    def _set_timezone(datetime_today, timezone):
        timezone = pytz.timezone(timezone)
        return timezone.localize(datetime_today)

    def now(self, timezone=None):
        self.datetime_today = datetime.datetime.today()
        if timezone:
            self.datetime_today = self._set_timezone(self.datetime_today, timezone)
        return self

    def today(self, timezone=None):
        self.datetime_today = datetime.datetime.today().replace(hour=0, minute=0, second=0)
        if timezone:
            self.datetime_today = self._set_timezone(self.datetime_today, timezone)
        return self

    def yesterday(self, timezone=None):
        self.datetime_today = datetime.datetime.today().replace(hour=0, minute=0, second=0) - datetime.timedelta(days=1)
        if timezone:
            self.datetime_today = self._set_timezone(self.datetime_today, timezone)
        return self

    def tomorrow(self, timezone=None):
        self.datetime_today = datetime.datetime.today().replace(hour=0, minute=0, second=0) + datetime.timedelta(days=1)
        if timezone:
            self.datetime_today = self._set_timezone(self.datetime_today, timezone)
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

    @property
    def to_date_time_string(self):
        return self.datetime_today.strftime("%Y-%m-%d, %H:%M:%S")

    @property
    def to_date_string(self):
        return self.datetime_today.strftime("%Y-%m-%d")

    @property
    def to_atom_string(self):
        return self.datetime_today.astimezone().replace(tzinfo=datetime.timezone.utc).isoformat()

    @property
    def to_iso8601_string(self):
        return self.datetime_today.astimezone().replace(microsecond=0).isoformat()

    @property
    def tz_name(self):
        return self.datetime_today.tzname()

    def utc_offset(self):
        # TODO create set utc offset
        return self.datetime_today.utcoffset().total_seconds() / 60

    @property
    def tz_info(self):
        if self.datetime_today.tzinfo:
            return str(self.datetime_today.tzinfo)
