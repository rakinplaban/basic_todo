from . import views
from django.urls import path

urlpatterns = [
    path('tasks', views.TodoView.as_view({'get': 'list', 'post': 'create'}), name='tasks'),
]