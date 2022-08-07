from django.contrib.auth import get_user_model
from django.test import TestCase


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
