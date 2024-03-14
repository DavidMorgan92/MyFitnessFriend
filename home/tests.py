from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from . import views


class IndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')

    def tearDown(self):
        self.user.delete()
        return super().tearDown()

    def test_view_is_rendered_by_correct_view_func(self):
        response = self.client.get(reverse('home_index'))
        self.assertEqual(response.resolver_match.func, views.index)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home_index'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_view_contains_brand_link_when_unauthenticated(self):
        response = self.client.get(reverse('home_index'))
        self.assertContains(
            response, f'<a class="navbar-brand" href="{reverse('home_index')}">My Fitness Friend</a>')

    def test_view_contains_home_nav_link_when_unauthenticated(self):
        response = self.client.get(reverse('home_index'))
        self.assertContains(
            response, f'<a class="nav-link active" aria-current="page" href="{reverse('home_index')}">Home</a>', html=True)

    def test_view_contains_food_diary_nav_link_when_unauthenticated(self):
        response = self.client.get(reverse('home_index'))
        self.assertContains(
            response, f'<a class="nav-link" href="{reverse('food_diary_index')}">Food Diary</a>', html=True)

    def test_view_contains_brand_link_when_authenticated(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('home_index'))
        self.assertContains(
            response, f'<a class="navbar-brand" href="{reverse('home_index')}">My Fitness Friend</a>')

    def test_view_contains_home_nav_link_when_authenticated(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('home_index'))
        self.assertContains(
            response, f'<a class="nav-link active" aria-current="page" href="{reverse('home_index')}">Home</a>', html=True)

    def test_view_contains_food_diary_nav_link_when_authenticated(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('home_index'))
        self.assertContains(
            response, f'<a class="nav-link" href="{reverse('food_diary_index')}">Food Diary</a>', html=True)

    def test_view_contains_login_nav_link_when_unauthenticated(self):
        response = self.client.get(reverse('home_index'))
        self.assertContains(
            response, f'<a class="nav-link" href="{reverse('account_login')}">Log In</a>', html=True)

    def test_view_contains_register_nav_link_when_unauthenticated(self):
        response = self.client.get(reverse('home_index'))
        self.assertContains(
            response, f'<a class="nav-link" href="{reverse('account_signup')}">Register</a>', html=True)

    def test_view_does_not_contain_login_nav_link_when_authenticated(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('home_index'))
        self.assertNotContains(
            response, f'<a class="nav-link" href="{reverse('account_login')}">Log In</a>', html=True)

    def test_view_does_not_contain_register_nav_link_when_authenticated(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('home_index'))
        self.assertNotContains(
            response, f'<a class="nav-link" href="{reverse('account_signup')}">Register</a>', html=True)

    def test_view_contains_profile_nav_link_when_authenticated(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('home_index'))
        self.assertContains(
            response, f'<a class="nav-link" href="{reverse('my_profile_index')}">My Profile</a>', html=True)

    def test_view_contains_logout_nav_link_when_authenticated(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('home_index'))
        self.assertContains(
            response, f'<a class="nav-link" href="{reverse('account_logout')}">Log Out</a>', html=True)

    def test_view_does_not_contain_profile_nav_link_when_unauthenticated(self):
        response = self.client.get(reverse('home_index'))
        self.assertNotContains(
            response, f'<a class="nav-link" href="{reverse('my_profile_index')}">My Profile</a>', html=True)

    def test_view_does_not_contain_logout_nav_link_when_unauthenticated(self):
        response = self.client.get(reverse('home_index'))
        self.assertNotContains(
            response, f'<a class="nav-link" href="{reverse('account_logout')}">Log Out</a>', html=True)
