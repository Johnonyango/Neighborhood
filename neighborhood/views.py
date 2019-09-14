from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect


# Create your views here.
def welcome(request):
    return render(request,'index.html')

def login(request):
    return render(request, 'registration/registration.html')

def profile(request):
    return render(request, 'profile.html')

def business(request):
  john = request.user.id
  profile = Profile.objects.get(user=john)

  if request.method == 'POST':
    form = NewBusinessForm(request.POST)
    if form.is_valid():
      business = form.save(commit=False)
      business.neighbourhood = profile.neighbourhood
      business.save()
    return redirect('business')

  else:
    form = NewBusinessForm()

  return render(request, 'business.html',{'form':form,'profile':profile})


  else:
    form = NewBusinessForm()

    return render(request, 'businesses.html')

def services(request):
    return render(request, 'govern.html')

def posts(request):
    return render(request, 'posts.html')

def change_hood(request):
    return render(request, 'change.html')


