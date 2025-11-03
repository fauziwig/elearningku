# E-Learning Platform | ElearningKu

## Overview
ElearningKu is a web application designed to facilitate online learning. It provides features for managing courses, quizzes, and user interactions, making it an ideal solution for educational institutions and independent educators.

## Features
- Course management
- User registration and authentication
- Interactive quizzes with scoring system
- Progress tracking
- Admin panel for content management
- User profile management
- Comprehensive unit tests with 91% coverage

## Project Structure
```
e_learning_platform/
├── e_learning_platform/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── courses/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── test_models.py
│   ├── test_views.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── test_models.py
│   ├── test_views.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── conftest.py
├── pytest.ini
├── manage.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd e_learning_platform
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project
1. Apply migrations:
   ```bash
   python manage.py migrate
   ```
2. Run the development server:
   ```bash
   python manage.py runserver 8080
   ```
   Atau gunakan script helper:
   ```bash
   ./run_server.sh
   ```
   atau
   ```bash
   python run_server.py
   ```
3. Access the application at `http://127.0.0.1:8080/`.

---

## Testing

### Overview
Project ini dilengkapi dengan comprehensive unit tests menggunakan pytest, mencapai **91% test coverage**.

### Test Statistics
- ✅ **49 unit tests** covering all major features
- ✅ **91% overall coverage** (100% for models, 86-96% for views)
- ✅ Tests run in ~30 seconds with isolated database
- ✅ Automatic fixtures and cleanup

### Installing Test Dependencies

```bash
pip install pytest pytest-django pytest-cov
```

Or using virtual environment:
```bash
venv/bin/pip install pytest pytest-django pytest-cov
```

### Running Tests

#### Run all tests
```bash
pytest
```

#### Run tests for specific app
```bash
# Test users app only
pytest users/

# Test courses app only
pytest courses/
```

#### Run specific test file
```bash
pytest users/test_models.py
pytest users/test_views.py
pytest courses/test_models.py
pytest courses/test_views.py
```

#### Run with verbose output
```bash
pytest -v
```

#### Run with coverage report
```bash
pytest --cov=users --cov=courses
pytest --cov=users --cov=courses --cov-report=html
pytest --cov=users --cov=courses --cov-report=term-missing
```

#### Run tests quietly (summary only)
```bash
pytest -q
```

### Test Structure

#### Users App Tests (19 tests)

**users/test_models.py** - Tests for CustomUser, UserProfile, and UserActivity models
- ✅ CustomUser creation and authentication
- ✅ Superuser creation with proper permissions
- ✅ User string representation
- ✅ User bio field functionality
- ✅ User profile picture field
- ✅ UserProfile creation and relationships
- ✅ UserProfile string representation
- ✅ UserActivity creation and tracking
- ✅ UserActivity string representation

**users/test_views.py** - Tests for authentication views
- ✅ Register page loading
- ✅ Register redirect for authenticated users
- ✅ Login page loading
- ✅ Login with valid credentials
- ✅ Login with invalid credentials
- ✅ Login redirect for authenticated users
- ✅ Login with next parameter
- ✅ Profile authentication requirement
- ✅ Profile page for authenticated users
- ✅ Logout functionality

#### Courses App Tests (30 tests)

**courses/test_models.py** - Tests for Material, Question, and Choice models
- ✅ Material creation with timestamps
- ✅ Material string representation
- ✅ Material with optional image field
- ✅ Question creation and relationships
- ✅ Question string representation
- ✅ Multiple questions per material
- ✅ Question cascade delete
- ✅ Choice creation with correctness flag
- ✅ Choice string representation
- ✅ Multiple choices per question
- ✅ Choice cascade delete

**courses/test_views.py** - Tests for course and quiz views
- ✅ Course list page loading
- ✅ Course list displays materials
- ✅ Course list when empty
- ✅ Course detail page loading
- ✅ Course detail content display
- ✅ Course detail with invalid ID
- ✅ Quiz detail page loading
- ✅ Quiz displays questions
- ✅ Quiz with invalid material ID
- ✅ Submit quiz with correct answer
- ✅ Submit quiz with wrong answer
- ✅ Submit quiz stores result in session
- ✅ Submit quiz GET method error
- ✅ Quiz result page with session data
- ✅ Quiz result redirect without session
- ✅ Quiz result clears session after display
- ✅ Quiz scoring - all correct answers
- ✅ Quiz scoring - all wrong answers
- ✅ Quiz scoring - partial correct answers

### Test Coverage Summary

```
Total Coverage: 91%

Key Areas:
- Models: 100% coverage
- Views: 86-96% coverage
- URLs: 100% coverage
- Admin: 100% coverage
```

### Test Configuration

**pytest.ini** - Pytest configuration
- Django settings module integration
- Test file discovery patterns (test_*.py)
- Pytest options and markers

**conftest.py** - Shared test fixtures
- User creation fixtures
- Authenticated client fixture
- Material, Question, and Choice fixtures

### Test Features
- Tests use SQLite in-memory database for speed
- Each test runs in isolation with automatic database rollback
- Fixtures are automatically cleaned up after each test
- No manual setup/teardown required

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
