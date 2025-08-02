from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):

    def setUp(self):
        self.User = get_user_model()
        self.user = self.User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('testpassword'))

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_user_email_normalization(self):
        user = self.User.objects.create_user(
            username='testuser2',
            email='TESTUSER@EXAMPLE.COM',
            password='testpassword'
        )
        self.assertEqual(user.email, 'testuser@example.com')