from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse


class CustomerUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="tywin", email="tywin@gmail.com", password="lannister"
        )

        self.assertEqual(user.username, "tywin")
        self.assertEqual(user.email, "tywin@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="oberyn", email="oberyn@gmail.com", password="martell"
        )

        self.assertEqual(admin_user.username, "oberyn")
        self.assertEqual(admin_user.email, "oberyn@gmail.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    username = "melisandre"
    email = "melisandre@gmail.com"

    def setUp(self):
        url = reverse("account_signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "account/signup.html")
        self.assertContains(self.response, "Sign up")
        self.assertNotContains(self.response, "Possibility")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
