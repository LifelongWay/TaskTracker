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

class OrderForm(forms.Form):
    ORDER_CHOICES = [
        ('-priority', 'High Priority First'),
        ('priority', 'Low Priority First'),
        ('difficulty', 'Easy Tasks First'),
        ('-difficulty', 'Hard Tasks First'),
        ('-due_date', 'Upcoming Deadlines'),
        ('due_date', 'Later Deadlines'),
    ]
    
    order = forms.ChoiceField(choices=ORDER_CHOICES,
    widget = forms.Select(attrs={'class' : 'form-input', 'onchange' : 'this.form.submit();'}))