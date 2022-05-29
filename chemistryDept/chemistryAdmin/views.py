from django.shortcuts import render

def home(request):
    return render(request, 'chemistryAdmin/index.html')

def login(request):
    return render(request, 'chemistryAdmin/login.html')

def bschemistry(request):
    return render(request, 'chemistryAdmin/bschemistry.html')

def bschemical(request):
    return render(request, 'chemistryAdmin/bschemical.html')

def mschemistry(request):
    return render(request, 'chemistryAdmin/mschemistry.html')

def msbiomedical(request):
    return render(request, 'chemistryAdmin/msbiomedical.html')

def certificateprograms(request):
    return render(request, 'chemistryAdmin/certificateprograms.html')

def faculty(request):
    return render(request, 'chemistryAdmin/faculty.html')

def staff(request):
    return render(request, 'chemistryAdmin/staff.html')

def student(request):
    return render(request, 'chemistryAdmin/student.html')

def errorpage(request):
    return render(request, 'chemistryAdmin/404.html')

def contactpage(request):
    return render(request, 'chemistryAdmin/contact.html')

def AdminPanel(request):
    return render(request, 'AdminPanel/index.html')


