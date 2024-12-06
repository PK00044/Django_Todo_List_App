from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import ToDo


class ToDoTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo_data = {
            "title": "Test Task",
            "description": "A test task description",
            "due_date": "2024-12-05",
            "tags": "test,task",
            "status": "OPEN",
        }
        self.todo = ToDo.objects.create(**self.todo_data)

    def test_create_todo(self):
        response = self.client.post(reverse('todo-list-create'), self.todo_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_todos(self):
        response = self.client.get(reverse('todo-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_todo(self):
        response = self.client.get(reverse('todo-detail', kwargs={'pk': self.todo.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_todo(self):
        updated_data = {"title": "Updated Task"}
        response = self.client.patch(reverse('todo-detail', kwargs={'pk': self.todo.id}), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo(self):
        response = self.client.delete(reverse('todo-detail', kwargs={'pk': self.todo.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
