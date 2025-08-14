from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import TaskListForm, TaskForm, OrderForm
from django.db.models import F, ExpressionWrapper, fields
from .models import List, Task
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

@login_required(login_url='users:login')
def remove_task_list(request, list_id):
    list_to_delete = get_object_or_404(List, pk = list_id)
    list_to_delete.delete()
    return redirect('tasks:my-task-lists')

@login_required(login_url = 'users:login')
def task_list(request, list_id):
    user = request.user

    # form for changing dropdown of order
    order_form = OrderForm()
    order_by = '-priority'
    # user changed order by - dropdown value
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_by = order_form.cleaned_data['order']
        else:
            # error
            pass
    
    list = List.objects.filter(user = user).get(pk = list_id)
    # if order_by == 'due_date':
    #     tasks
    # else:
    
    if order_by == 'due_date': tasks = list.tasks.all().annotate(
        remaining_time = (ExpressionWrapper((F('due_date') - timezone.now()), output_field= fields.DurationField()))
    ).order_by(F('remaining_time').desc(nulls_last = True))
    elif order_by == '-due_date' : tasks = list.tasks.all().annotate(
        remaining_time = (ExpressionWrapper((F('due_date') - timezone.now()), output_field= fields.DurationField()))
    ).order_by(F('remaining_time').asc(nulls_last = True))
    else:
        tasks = list.tasks.all().order_by(order_by)
    return render(request, 'tasks/task_list.html', {"list": list, "tasks": tasks, "order_form": order_form})

@login_required(login_url = 'users:login')
def remove_task(request, list_id, task_id):
    user = request.user
    list = List.objects.filter(user = user).get(pk = list_id)
    task_to_delete = list.tasks.get(pk = task_id)
    task_to_delete.delete()
    return redirect('tasks:my-task-list', list_id=list_id)

@login_required(login_url='users:login')
def create_task(request, list_id):
    # make form
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit = False)
            new_task.list = List.objects.get(pk = list_id)
            new_task.save()
            return redirect('tasks:my-task-list', list_id=list_id)
        else:
            return render(request, 'tasks/task_create.html', {'list_id': list_id, 'form': form, 'error': True})
    form = TaskForm()
    return render(request, 'tasks/task_create.html', {'list_id': list_id, 'form': form})

@login_required(login_url='users:login')
def edit_task(request, list_id, task_id):
    list_instance = get_object_or_404(List, pk = list_id)
    task_instance = get_object_or_404(Task, pk = task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task_instance)
        form.save() # since already has user assigned to user field (not first edit)
        return redirect('tasks:my-task-list', list_id = list_id )
    form = TaskForm(instance = task_instance)
    return render(request, 'tasks/task_list.html', {'list': list_instance, 'form': form, 'editing_task_id': task_id})