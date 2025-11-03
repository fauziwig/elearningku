import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
class TestRegisterView:
    def test_register_page_loads(self, client):
        url = reverse('register')
        response = client.get(url)
        assert response.status_code == 200
        assert 'form' in response.context

    def test_register_redirects_if_authenticated(self, authenticated_client):
        url = reverse('register')
        response = authenticated_client.get(url)
        assert response.status_code == 302

@pytest.mark.django_db
class TestLoginView:
    def test_login_page_loads(self, client):
        url = reverse('login')
        response = client.get(url)
        assert response.status_code == 200
        assert 'form' in response.context

    def test_login_with_valid_credentials(self, client, create_user, user_data):
        url = reverse('login')
        data = {
            'username': user_data['username'],
            'password': user_data['password']
        }
        response = client.post(url, data)
        assert response.status_code == 302

    def test_login_with_invalid_credentials(self, client):
        url = reverse('login')
        data = {
            'username': 'wronguser',
            'password': 'wrongpass'
        }
        response = client.post(url, data)
        assert response.status_code == 200

    def test_login_redirects_if_authenticated(self, authenticated_client):
        url = reverse('login')
        response = authenticated_client.get(url)
        assert response.status_code == 302

    def test_login_with_next_parameter(self, client, create_user, user_data):
        url = reverse('login') + '?next=/courses/'
        data = {
            'username': user_data['username'],
            'password': user_data['password']
        }
        response = client.post(url, data)
        assert response.status_code == 302

@pytest.mark.django_db
class TestProfileView:
    def test_profile_requires_authentication(self, client):
        url = reverse('profile')
        response = client.get(url)
        assert response.status_code == 302
        assert '/users/login/' in response.url

    def test_profile_page_loads_for_authenticated_user(self, authenticated_client):
        url = reverse('profile')
        response = authenticated_client.get(url)
        assert response.status_code == 200

@pytest.mark.django_db
class TestLogoutView:
    def test_logout_redirects(self, authenticated_client):
        url = reverse('logout')
        response = authenticated_client.get(url)
        assert response.status_code == 302
