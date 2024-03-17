import datetime
import re
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from . import views
from .models import FoodDiary, FoodDiaryEntry
from url_tools import reverse_with_params
from .converters import DateConverter


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


class IndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')

    def tearDown(self):
        self.user.delete()
        return super().tearDown()

    def test_view_redirects_to_login(self):
        response = self.client.get(reverse('food_diary_index'), follow=True)
        self.assertRedirects(response, reverse_with_params(
            'account_login', get={'next': '/food_diary/'}))

    def test_view_is_rendered_by_correct_view_func(self):
        response = self.client.get(reverse('food_diary_index'))
        self.assertEqual(response.resolver_match.func, views.index)

    def test_view_uses_correct_template(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('food_diary_index'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'food_diary/index.html')

    def test_food_diary_nav_link_is_active(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('food_diary_index'))
        self.assertContains(response, f'<a class="nav-link active" aria-current="page" href="{reverse(
            'food_diary_index')}">Food Diary</a>', html=True)


class DeleteEntryTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')

    def tearDown(self):
        self.user.delete()
        return super().tearDown()

    def test_view_redirects_to_login(self):
        response = self.client.get(
            reverse('food_diary_delete_entry', args=[datetime.date(2001, 1, 1), 1]), follow=True)
        self.assertRedirects(response, reverse_with_params(
            'account_login', get={'next': '/food_diary/delete/2001-01-01/1'}))

    def test_view_is_rendered_by_correct_view_func(self):
        response = self.client.get(
            reverse('food_diary_delete_entry', args=[datetime.date(2001, 1, 1), 1]))
        self.assertEqual(response.resolver_match.func, views.delete_entry)

    def test_view_returns_404_if_food_diary_does_not_exist_for_authenticated_user(self):
        other_user = User.objects.create_user(
            username='user2', password='user2')
        FoodDiary.objects.create(
            id=1, owner=other_user, date=datetime.date(2001, 1, 1))
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(
            reverse('food_diary_delete_entry', args=[datetime.date(2001, 1, 1), 1]))
        self.assertEqual(response.status_code, 404)

    def test_view_returns_404_if_food_diary_does_not_exist_for_given_date(self):
        FoodDiary.objects.create(
            id=1, owner=self.user, date=datetime.date(2001, 1, 2))
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(
            reverse('food_diary_delete_entry', args=[datetime.date(2001, 1, 1), 1]))
        self.assertEqual(response.status_code, 404)

    def test_view_returns_404_if_entry_does_not_exist_for_given_food_diary(self):
        FoodDiary.objects.create(
            id=1, owner=self.user, date=datetime.date(2001, 1, 1))
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(
            reverse('food_diary_delete_entry', args=[datetime.date(2001, 1, 1), 1]))
        self.assertEqual(response.status_code, 404)

    def test_view_deletes_entry(self):
        food_diary = FoodDiary.objects.create(
            id=1, owner=self.user, date=datetime.date(2001, 1, 1))
        FoodDiaryEntry.objects.create(id=1, food_diary=food_diary, name='test', meal=FoodDiaryEntry.Meal.BREAKFAST, calories=1,
                                      carbs_grams=1, fat_grams=1, protein_grams=1, sodium_milligrams=1, sugar_grams=1)
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(
            reverse('food_diary_delete_entry', args=[datetime.date(2001, 1, 1), 1]), follow=True)
        self.assertRedirects(response, reverse_with_params(
            'food_diary_index', get={'date': datetime.date(2001, 1, 1)}))
        entry = list(FoodDiaryEntry.objects.filter(id=1))
        self.assertEqual(len(entry), 0)
