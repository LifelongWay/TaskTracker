from django.db import models

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120)
    date_added = models.DateTimeField(auto_now=True)
