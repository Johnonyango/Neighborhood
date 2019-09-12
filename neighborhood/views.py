from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request,'index.html')

def login(request):
    return render(request, 'registration/registration.html')

def profile(request):
    return render(request, 'profile.html')