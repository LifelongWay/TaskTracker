from django.shortcuts import render

# Create your views here.
def all_tasks(request):
    context = {
        'active_page': 'my-tasks'
    }
    return render(request, 'tasks/all-tasks.html', context)