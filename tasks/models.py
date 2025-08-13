from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class List(models.Model): # task list
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'lists')
    name = models.CharField(max_length=100)


    def __str__(self):
        return f"List {self.user.username} of User: {self.user.username}"
    

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Difficult'),
    ]

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name = 'tasks')
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    due_date = models.DateTimeField(blank = True, null = True)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default= 2)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES ,default = 1)

    def __str__(self):
        return self.title