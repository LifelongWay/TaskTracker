from django.shortcuts import render, redirect
from .forms import TaskListForm, TaskForm
from .models import List
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url= 'users:login')
def all_tasks(request):
    user = request.user 

    context = {
        'active_page': 'my-tasks',
        'task_lists': List.objects.filter(user = user), 
    }    
    
    return render(request, 'tasks/all-tasks.html', context)

@login_required(login_url='users:login')
def new_task_list(request):
    user = request.user
    context = {
        'active_page': 'my-tasks',
        'task_lists': List.objects.filter(user=user),
    }

    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = user
            new_list.save()  # saving new list
            return redirect('tasks:my-tasks')  # <-- move inside here
        else:
            context['form'] = form  # show errors if invalid
            return render(request, 'tasks/new-list.html', context)

    form = TaskListForm()
    context['form'] = form
    return render(request, 'tasks/new-list.html', context)
