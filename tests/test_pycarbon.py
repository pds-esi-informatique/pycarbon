import unittest

import datetime

from pycarbon.pycarbon import PyCarbon

py_carbon = PyCarbon()


class MyTestCase(unittest.TestCase):
    def test_now(self):
        self.assertEqual(type(py_carbon.now().datetime_today), datetime.datetime)

    def test_today(self):
        self.assertEqual(type(py_carbon.today().datetime_today), datetime.datetime)

    def test_yesterday(self):
        self.assertEqual(type(py_carbon.yesterday().datetime_today), datetime.datetime)

    def test_tomorrow(self):
        self.assertEqual(type(py_carbon.tomorrow().datetime_today), datetime.datetime)


if __name__ == '__main__':
    unittest.main()
