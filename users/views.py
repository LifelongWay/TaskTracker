from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:my-tasks')
    form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            # form is filled correctly
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username = username, password = password)
            if user is not None:
                # credentials are right - create session
                login(request, user)
                return redirect('tasks:my-task-lists')
            else:
                return render(request, 'users/login.html', {'form': form, 'error': True})
        else:
            return render(request, 'users/login.html', {'form': form, 'error': True})
    form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form, 'error': False})

def logout_view(request):
    logout(request)
    return redirect('homepage')