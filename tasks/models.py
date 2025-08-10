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
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('difficult', 'Difficult'),
    ]

    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name = 'tasks')
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    due_date = models.DateTimeField(blank = True, null = True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES ,default = 'easy')

    def __str__(self):
        return self.title