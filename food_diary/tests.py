from django.test import TestCase
from .converters import DateConverter
import datetime
import re


class DateConverterTests(TestCase):
    def test_to_python_returns_date_given_valid_string(self):
        date_converter = DateConverter()
        date = date_converter.to_python('2001-05-09')
        self.assertEqual(2001, date.year)
        self.assertEqual(5, date.month)
        self.assertEqual(9, date.day)

    def test_to_url_returns_formatted_string_given_date(self):
        date_converter = DateConverter()
        date = date_converter.to_url(datetime.date(2001, 5, 9))
        self.assertEqual('2001-05-09', date)

    def test_regex_matches_given_valid_string(self):
        match = re.fullmatch(DateConverter.regex, '2001-05-09')
        self.assertIsNotNone(match)

    def test_regex_fails_match_given_invalid_string(self):
        match = re.fullmatch(DateConverter.regex, 'invalid date')
        self.assertIsNone(match)
