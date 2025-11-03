import pytest
from django.contrib.auth import get_user_model
from users.models import UserProfile, UserActivity

User = get_user_model()

@pytest.mark.django_db
class TestCustomUser:
    def test_create_user(self):
        user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )
        assert user.username == 'testuser'
        assert user.email == 'test@example.com'
        assert user.check_password('testpass123')
        assert user.is_active

    def test_create_superuser(self):
        admin = User.objects.create_superuser(
            username='admin',
            password='adminpass123',
            email='admin@example.com'
        )
        assert admin.is_superuser
        assert admin.is_staff

    def test_user_str_representation(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        assert str(user) == 'testuser'

    def test_user_bio_field(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        user.bio = 'This is my bio'
        user.save()
        assert user.bio == 'This is my bio'

    def test_user_profile_picture_field(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        assert not user.profile_picture

@pytest.mark.django_db
class TestUserProfile:
    def test_create_user_profile(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        profile = UserProfile.objects.create(
            user=user,
            location='Jakarta'
        )
        assert profile.user == user
        assert profile.location == 'Jakarta'

    def test_user_profile_str_representation(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        profile = UserProfile.objects.create(user=user)
        assert str(profile) == 'testuser'

@pytest.mark.django_db
class TestUserActivity:
    def test_create_user_activity(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        activity = UserActivity.objects.create(
            user=user,
            activity_type='login'
        )
        assert activity.user == user
        assert activity.activity_type == 'login'
        assert activity.timestamp is not None

    def test_user_activity_str_representation(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        activity = UserActivity.objects.create(
            user=user,
            activity_type='course_view'
        )
        assert 'course_view' in str(activity)
        assert 'testuser' in str(activity)
