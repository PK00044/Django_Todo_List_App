from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer


class ToDoListCreateView(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


class ToDoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the To-Do App API! Visit /api/todos/ to interact.")
