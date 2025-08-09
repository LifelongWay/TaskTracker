from django.shortcuts import render

def homepage(request):
    context = {
        'active_page': 'homepage'
    }
    return render(request, 'todoweb/homepage.html', context)