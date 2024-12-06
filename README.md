# To-Do List App
A Django-based REST API application for managing tasks.

## Features
- Create, read, update, and delete tasks.
- Secure access with Basic Authentication.
- 100% test coverage using Django's test framework.
- CI/CD pipeline with GitHub Actions.

## Requirements
- Python 3.11+
- Django 4.2.7
- Django Rest Framework 3.14.0

## Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd todo_project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints
- `GET /api/todos/` - List all tasks.
- `POST /api/todos/` - Create a new task.
- `GET /api/todos/<id>/` - Retrieve a task.
- `PUT /api/todos/<id>/` - Update a task.
- `DELETE /api/todos/<id>/` - Delete a task.

## Testing
Run tests using:
```bash
python manage.py test
```

## License
This project is for the AlgoBulls Internship Assignment.
