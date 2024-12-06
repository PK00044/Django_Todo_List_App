from django.contrib import admin
from django.urls import path, include
from todo_project.todo.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
]
