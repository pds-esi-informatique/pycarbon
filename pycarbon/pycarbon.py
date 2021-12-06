import datetime
import calendar
import re
import pytz

MONTHS = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06", "july": "07",
          "august": "08", "september": "09", "october": "10", "november": "11", "december": "12"}


class PyCarbon:
    def __init__(self, date: str = None):
        self.datetime_today = None
        if date:
            self.datetime_today = datetime.datetime.today()
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
        """
        Put the date in a standard format and readable for everyone, add the field if a timezeone has been added
        :return: The formatted date
        """
        if self.datetime_today and type(self.datetime_today) is datetime.datetime:
            if self.datetime_today.tzname():
                return self.datetime_today.strftime("%Y-%m-%d, %H:%M:%S ") + str(self.datetime_today.tzinfo)
            else:
                return self.datetime_today.strftime("%Y-%m-%d, %H:%M:%S")

    @staticmethod
    def _positive_parameter_number(number: int):
        """
        Allows not to have an error when the person indicates a number always returns a positive
        :param number: an integer
        :return: positive integer
        """
        return abs(number)

    @staticmethod
    def _calculate_months(datetime_today: datetime.datetime, months: int):
        """
        Allows you to calculate a month based on the existing date
        https://stackoverflow.com/questions/4130922/how-to-increment-datetime-by-custom-months-in-python-without-using-library/23506665
        :return: The date with the number of months in addition
        """
        month = datetime_today.month - 1 + months
        year = datetime_today.year + month // 12
        month = month % 12 + 1
        day = min(datetime_today.day, calendar.monthrange(year, month)[1])
        return datetime_today.replace(year=year, month=month, day=day)

    @staticmethod
    def _calculate_days(datetime_today: datetime.datetime, days: int):
        """
        Calculates the number of days added by the given date
        :param datetime_today: A date
        :param days: The number of days
        :return: The date with the number of days calculated
        """
        return datetime_today + datetime.timedelta(days=days)
    @staticmethod
    def _calculate_hours(datetime_today: datetime.datetime, hours: int):
        """
        Calculates the number of hours added by the given date
        :param datetime_today: A date
        :param days: The number of days
        :return: The date with the number of days calculated
        """
        return datetime_today + datetime.timedelta(hours=hours)
    @staticmethod
    def _set_timezone(datetime_today: datetime.datetime, timezone: str):
        """
        Allows you to add a timezone to a date
        :param datetime_today: A date
        :param timezone: The timezone to add
        :return: The date with the timezone in addition
        """
        timezone = pytz.timezone(timezone)
        return timezone.localize(datetime_today)

    def now(self, timezone: str = None):
        """
        Today's date and time
        :param timezone: If you need to set a timezone
        :return: Returns the object
        """
        self.datetime_today = datetime.datetime.today()
        if timezone:
            self.datetime_today = self._set_timezone(self.datetime_today, timezone)
        return self
    def today(self, timezone: str = None):
        """
        Today's date and first time
        :param timezone: If you need to set a timezone
        :return: Returns the object
        """
        self.datetime_today = datetime.datetime.today().replace(hour=0, minute=0, second=0)
        if timezone:
            self.datetime_today = self._set_timezone(self.datetime_today, timezone)
        return self

    def yesterday(self, timezone: str = None):
        """
        The previous day's date compared to today's date
        :param timezone: If you need to set a timezone
        :return: Returns the object
        """
        self.datetime_today = datetime.datetime.today().replace(hour=0, minute=0, second=0) - datetime.timedelta(days=1)
        if timezone:
            self.datetime_today = self._set_timezone(self.datetime_today, timezone)
        return self

    def tomorrow(self, timezone: str = None):
        """
        Next day's date compared to today's date
        :param timezone: If you need to set a timezone
        :return: Returns the object
        """
        self.datetime_today = datetime.datetime.today().replace(hour=0, minute=0, second=0) + datetime.timedelta(days=1)
        if timezone:
            self.datetime_today = self._set_timezone(self.datetime_today, timezone)
        return self
    def add_hour(self):
        """
        Add a hour to the date
        :return: Returns the object
        """
        self.datetime_today = self._calculate_hours(self.datetime_today,1)
        return self
    def add_hours(self, hours: int):
        """
        Add a hour to the date
        :return: Returns the object
        """
        self.datetime_today = self._calculate_hours(self.datetime_today,hours)
        return self
    def add_day(self):
        """
        Add a day to the date
        :return: Returns the object
        """
        self.datetime_today = self._calculate_days(self.datetime_today, 1)
        return self

    def add_days(self, days: int):
        """
        Add the number of days to the date
        :param days: Number of days
        :return: Returns the object
        """
        days = self._positive_parameter_number(days)
        self.datetime_today = self._calculate_days(self.datetime_today, days)
        return self

    def sub_day(self):
        """
        Remove a day from the date
        :return: Returns the object
        """
        self.datetime_today = self._calculate_days(self.datetime_today, -1)
        return self

    def sub_days(self, days: int):
        """
        Remove the number of days from the date
        :param days: Number of days
        :return: Returns the object
        """
        days = self._positive_parameter_number(days)
        self.datetime_today = self._calculate_days(self.datetime_today, -days)
        return self

    def add_month(self):
        """
        Add a month to the date
        :return: Returns the object
        """
        self.datetime_today = self._calculate_months(self.datetime_today, 1)
        return self

    def add_months(self, months: int):
        """
        Add months to the date
        :param months:  Number of months
        :return: Returns the object
        """
        months = self._positive_parameter_number(months)
        self.datetime_today = self._calculate_months(self.datetime_today, months)
        return self

    def sub_month(self):
        """
        Remove one month from the date
        :return: Returns the object
        """
        self.datetime_today = self._calculate_months(self.datetime_today, -1)
        return self

    def sub_months(self, months: int):
        """
        Remove months from the date
        :param months: Number of months
        :return: Returns the object
        """
        months = self._positive_parameter_number(months)
        self.datetime_today = self._calculate_months(self.datetime_today, -months)
        return self

    def first_of_month(self):
        """
        Set the first day of the month to the date
        :return: Returns the object
        """
        self.datetime_today = self.datetime_today.replace(day=1)
        return self

    def start_of_month(self):
        """
        Set the first day of the month to the first hour
        :return: Returns the object
        """
        self.datetime_today = self.datetime_today.replace(day=1, hour=0, minute=0, second=0)
        return self

    @property
    def to_date_time_string(self):
        """
        Returns the date and time in standard string format from the date
        :return: the date and time in standard string format
        """
        return self.datetime_today.strftime("%Y-%m-%d, %H:%M:%S")

    @property
    def to_date_string(self):
        """
        return the date in standard string format from the date
        :return: the date in standard string format
        """
        return self.datetime_today.strftime("%Y-%m-%d")

    @property
    def to_atom_string(self):
        """
        Returns the date time with the atomic time in iso 8601 format from the date
        """
        return self.datetime_today.astimezone().replace(tzinfo=datetime.timezone.utc).isoformat()

    @property
    def to_iso8601_string(self):
        """
        returns date and time in iso format 8601 from the date
        :return:  date and time in iso format 8601
        """
        return self.datetime_today.astimezone().replace(microsecond=0).isoformat()

    @property
    def tz_name(self):
        """
        Return the timezone name from the date
        :return: timezone name
        """
        return self.datetime_today.tzname()

    def utc_offset(self):
        """
        Returns utc offset from the date
        :return: utc offset
        """
        # TODO create set utc offset
        return self.datetime_today.utcoffset().total_seconds() / 60

    @property
    def tz_info(self):
        """
        Returns the time zone info of the date
        :return: timezone info
        """
        if self.datetime_today.tzinfo:
            return str(self.datetime_today.tzinfo)
