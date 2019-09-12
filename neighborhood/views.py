from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request,'index.html')

def login(request):
    return render(request, 'registration/registration.html')

def profile(request):
    return render(request, 'profile.html')

def business(request):
    return render(request, 'businesses.html')

def services(request):
    return render(request, 'govern.html')

def posts(request):
    return render(request, 'posts.html')


