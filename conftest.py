import pytest
from django.contrib.auth import get_user_model
from courses.models import Material, Question, Choice

User = get_user_model()

@pytest.fixture
def user_data():
    return {
        'username': 'testuser',
        'password': 'testpass123',
        'email': 'test@example.com'
    }

@pytest.fixture
def create_user(db, user_data):
    user = User.objects.create_user(
        username=user_data['username'],
        password=user_data['password'],
        email=user_data['email']
    )
    return user

@pytest.fixture
def authenticated_client(client, create_user, user_data):
    client.login(username=user_data['username'], password=user_data['password'])
    return client

@pytest.fixture
def material(db):
    return Material.objects.create(
        title='Test Material',
        content='This is test content for the material.'
    )

@pytest.fixture
def question(db, material):
    return Question.objects.create(
        material=material,
        question_text='What is the test question?'
    )

@pytest.fixture
def choices(db, question):
    choice1 = Choice.objects.create(
        question=question,
        choice_text='Correct Answer',
        is_correct=True
    )
    choice2 = Choice.objects.create(
        question=question,
        choice_text='Wrong Answer 1',
        is_correct=False
    )
    choice3 = Choice.objects.create(
        question=question,
        choice_text='Wrong Answer 2',
        is_correct=False
    )
    return [choice1, choice2, choice3]
