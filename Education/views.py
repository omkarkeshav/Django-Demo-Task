from django.shortcuts import render

# Create your views here.

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Admin(request):
    return render(request, 'adminlogin.html')

def Student(request):
    return render(request, 'studentlogin.html')

def Index(request):
    return render(request, 'index.html')