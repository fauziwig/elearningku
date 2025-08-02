# E-Learning Platform

## Overview
The E-Learning Platform is a web application designed to facilitate online learning. It provides features for managing courses, quizzes, and user interactions, making it an ideal solution for educational institutions and independent educators.

## Features
- Course management
- User registration and authentication
- Interactive quizzes
- Progress tracking
- Admin panel for content management

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
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd e_learning_platform
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Project
1. Apply migrations:
   ```
   python manage.py migrate
   ```
2. Run the development server:
   ```
   python manage.py runserver
   ```
3. Access the application at `http://127.0.0.1:8000/`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.