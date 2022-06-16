from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def AdminPanel(request):
    return render(request, 'AdminPanel/index.html')

def Adminprofile(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('Adminprofile')
    else:
        form = UserRegisterForm()
    return render(request, 'AdminPanel/profile.html', {'form': form})

def people(request):
    return render(request, 'AdminPanel/people.html')

def blank(request):
    return render(request, 'AdminPanel/blank.html')
