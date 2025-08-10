from django.shortcuts import render, redirect
from .forms import TaskListForm, TaskForm
from .models import List
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url= 'users:login')
def all_tasks(request):
    user = request.user 

    context = {
        'active_page': 'my-task-lists',
        'task_lists': List.objects.filter(user = user), 
    }    
    
    return render(request, 'tasks/task_lists.html', context)

@login_required(login_url='users:login')
def new_task_list(request):
    user = request.user
    context = {
        'active_page': 'my-task-lists',
        'task_lists': List.objects.filter(user=user),
    }

    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = user
            new_list.save()  # saving new list
            return redirect('tasks:my-task-lists')  # <-- move inside here
        else:
            context['form'] = form  # show errors if invalid
            return render(request, 'tasks/new-list.html', context)

    form = TaskListForm()
    context['form'] = form
    return render(request, 'tasks/new-list.html', context)


@login_required(login_url = 'users:login')
def task_list(request, id):
    user = request.user
    list = List.objects.filter(user = user).get(pk = id)
    return render(request, 'tasks/task_list.html', {"list": list})

@login_required(login_url = 'users:login')
def remove_task(request, list_id, task_id):
    user = request.user
    list = List.objects.filter(user = user).get(pk = list_id)
    task_to_delete = list.tasks.get(pk = task_id)
    task_to_delete.delete()
    return redirect('tasks:my-task-list', id=list_id)