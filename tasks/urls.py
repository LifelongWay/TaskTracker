from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('my-task-lists/', views.all_tasks, name = 'my-task-lists'),
    path('create-list/', views.new_task_list, name = 'new-list'),
    path('my-tasks/<int:id>/', views.task_list, name = "my-task-list"),
    path('my-tasks/<int:list_id>/remove/task/id=<int:task_id>/', views.remove_task, name = "remove-task" ) 
]
