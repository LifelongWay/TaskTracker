from django import forms
from .models import List, Task

class TaskListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['name'] # don't forget to set user.username

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'difficulty', 'due_date']

        widgets = {
            'due_date': forms.DateInput(attrs={ 'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
        }