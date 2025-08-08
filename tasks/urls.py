from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('my-tasks/', views.all_tasks, name = 'my-tasks')
]
