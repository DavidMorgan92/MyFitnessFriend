from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from . import views
from url_tools import reverse_with_params


class IndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='test')

    def tearDown(self):
        self.user.delete()
        return super().tearDown()

    def test_view_redirects_to_login(self):
        response = self.client.get(reverse('my_profile_index'), follow=True)
        self.assertRedirects(response, reverse_with_params(
            'account_login', get={'next': '/profile/'}))

    def test_view_is_rendered_by_correct_view_func(self):
        response = self.client.get(reverse('my_profile_index'))
        self.assertEqual(response.resolver_match.func, views.index)

    def test_view_uses_correct_template(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('my_profile_index'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'my_profile/index.html')

    def test_view_has_link_to_account_change_password(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('my_profile_index'))
        self.assertContains(response, f'<a href="{reverse(
            'account_change_password')}" class="btn btn-link">Change password</a>')

    def test_view_has_link_to_account_email(self):
        login_success = self.client.login(username='test', password='test')
        self.assertTrue(login_success)
        response = self.client.get(reverse('my_profile_index'))
        self.assertContains(response, f'<a href="{reverse(
            'account_email')}" class="btn btn-link">Manage email accounts</a>')
