from django.shortcuts import render

def AdminPanel(request):
    return render(request, 'AdminPanel/index.html')

def Adminprofile(request):
    return render(request, 'AdminPanel/profile.html')

def blank(request):
    return render(request, 'AdminPanel/blank.html')
