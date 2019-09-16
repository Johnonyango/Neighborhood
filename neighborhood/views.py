from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .forms import NeighForm, NewBusinessForm, ProfileForm,NewCommentForm, ContactForm, NewPostForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import NeighForm, NewBusinessForm, ProfileForm,NewCommentForm, ContactForm, NewPostForm
from .models import Neighbourhood, Business, Profile,NeighLetterRecipients,Post,Comment
# from .email import send_welcome_email
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializer import NeighbourhoodSerializer, ProfileSerializer
from .forms import NeighLetterForm
from .models import Profile, Post, Comment, Business, Neighbourhood, Contact
from django.db.models import Avg


# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    id = request.user.id
    profile = Profile.objects.get(user=id)
    return render(request, 'welcome.html',{'profile':profile})


def profile(request, id):
    john = request.user.id
    profile = Profile.objects.get(user=john)
    user = request.user

    neighbourhoods = Neighbourhood.objects.filter(post=john).order_by()
    neighbourhoodcount=neighbourhoods.count()
    
    return render(request, 'photos/profile.html',{'profile':profile,'user':user,'neighbourhoodcount':neighbourhoodcount,'neighbourhoods':neighbourhoods})

@login_required(login_url='/accounts/login/')
def myneighbourhood(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)
  neighbourhoods = Neighbourhood.objects.all().order_by()


  return render(request, 'neigh.html',{'profile':profile,'neighbourhoods':neighbourhoods})

@login_required(login_url='/accounts/login/')
def password(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)

  return render(request, 'password.html',{'profile':profile})




class BusinessList(APIView):
  def get(self, request, format=None):
    all_neighbourhoods = neighbourhood.objects.all()
    serializers = neighbourhoodserializer(all_neighbourhoods, many=True)
    return Response(serializers.data)

def mail(request):
  name = request.user.username
  email = request.user.email
  
  send_welcome_email(name,email)

  return HttpResponseRedirect(reverse('welcome'))

@login_required(login_url='/accounts/login/')
def newbusiness(request):
  user = request.user.id
  profile = Profile.objects.get(user=user)

  if request.method == 'POST':
    form = NewBusinessForm(request.POST)
    if form.is_valid():
      business = form.save(commit=False)
      business.neighbourhood = profile.neighbourhood
      business.save()
    return redirect('business')

  else:
    form = NewBusinessForm()

  return render(request, 'new_business.html',{'form':form,'profile':profile})


@login_required(login_url='/accounts/login/')
def newneighbourhood(request):
  user = request.user.id
  profile = Profile.objects.get(user=user)

  current_user = request.user
  current_username = request.user.username

  if request.method == 'POST':
    form = NeighForm(request.POST, request.FILES)
    if form.is_valid():
      neighbourhood = form.save(commit=False)
      neighbourhood.owner = current_user
      neighbourhood.neighbourhood = current_username
      neighbourhood.save()
    return redirect('myneighbourhood')

  else:
    form = NeighForm()
  
  return render(request, 'change_hood.html',{'form':form,'profile':profile})




@login_required(login_url='/accounts/login/')
def neighbourhood(request, id):
  user = request.user.id
  profile = Profile.objects.get(user=user)
  
  neighbourhoods = Neighbourhood.objects.get(pk=id)
  comments = Comment.objects.filter(neighbourhood=id).order_by()

  return render(request, 'photos/neighbor.html',{'profile':profile,'neighbourhood':neighbourhood,'comments':comments})

@login_required(login_url='/accounts/login/')
def post(request, id):
  user = request.user.id
  profile = Profile.objects.get(user=user)
  
  post = Post.objects.get(pk=id)
  comments = Comment.objects.filter(id=id).order_by()

  return render(request, 'photos/posts.html',{'profile':profile,'post':post,'comments':comments})

@login_required(login_url='/accounts/login/')
def mypost(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)
  posts = Post.objects.all().order_by()
  comments = Comment.objects.filter(id=id).order_by()

  return render(request, 'photos/posts.html',{'profile':profile,'posts':posts,'comments':comments})


@login_required(login_url='/accounts/login/')
def newprofile(request):
  user = request.user.id
  profile = Profile.objects.get(user=user)
  
  
  if request.method == 'POST':
    instance = get_object_or_404(Profile, user=user)
    form = ProfileForm(request.POST, request.FILES,instance=instance)
    if form.is_valid():
      form.save()
      

    return redirect('profile', frank)

  else:
    form = ProfileForm()

  return render(request, 'new_profile.html',{'form':form,'profile':profile})


@login_required(login_url='/accounts/login/')
def contacts(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)

  try:
    contacts = Contact.objects.filter(neighbourhood=profile.neighbourhood)

  except ObjectDoesNotExist:
    contacts = []

  return render(request, 'contacts.html',{'contacts':contacts,'profile':profile})


@login_required(login_url='/accounts/login/')
def newcontacts(request):
  user = request.user.id
  profile = Profile.objects.get(user=user)

  current_user = request.user
  current_username = request.user.username

  if request.method == 'POST':
    form = ContactForm(request.POST, request.FILES)
    if form.is_valid():
      contacts = form.save(commit=False)
      contacts.owner = current_user
      contacts.contacts = current_username
      contacts.save()
    return redirect('welcome')

  else:
    form = ContactForm()

  return render(request, 'new_contacts.html',{'form':form,'profile':profile})



@login_required(login_url='/accounts/login/')
def subscribe(request):
    id = request.user.id
    profile = Profile.objects.get(user=id)
    if request.method == 'POST':
        form = NeighLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NeighLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('index.html')
    else:
        form = NeighLetterForm()
    return render(request, 'subscribe.html', {'letterForm':form,'profile':profile})    

@login_required(login_url='/accounts/login/')
def newpost(request):
  user = request.user.id
  profile = Profile.objects.get(user=user)
  current_user = request.user
  current_username = request.user.username

  if request.method == 'POST':
    form = NewPostForm(request.POST, request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.poster = current_user
      post.postername = current_username
      post.neighbourhood = profile.neighbourhood
      post.save()
    return redirect('mypost')

  else:
    form = NewPostForm()

  return render(request, 'post.html',{'form':form,'profile':profile})




@login_required(login_url='/accounts/login/')
def newcomment(request):
  user = request.user.id
  profile = Profile.objects.get(user=user)
  idd = id

  current_username = request.user.username
  if request.method == 'POST':
    form = NewCommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)
      comment.postername = current_username
      comment.post = Post.objects.all()
      comment.save()
    return redirect('welcome')

  else:
    form = NewCommentForm()

  return render(request, 'newcomment.html',{'form':form,'profile':profile,'idd':idd})


@login_required(login_url='/accounts/login/')
def business(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)

  try:
    businesses = Business.objects.filter(neighbourhood=profile.neighbourhood)

  except ObjectDoesNotExist:
    businesses = []

  return render(request, 'business.html',{'businesses':businesses,'profile':profile})

@login_required(login_url='/accounts/login/')
def search(request):
  user = request.user.id
  profile = Profile.objects.get(user=user)


  if 'business' in request.GET and request.GET['business']:
    search_term = request.GET.get('business')
    message = f'{search_term}'
    title = 'Search Results'

    try:
      no_ws = search_term.strip()
      searched_business = Business.objects.filter(name__icontains = no_ws)
      searched_businesses = searched_business.filter(neighbourhood=profile.neighbourhood)

    except ObjectDoesNotExist:
      searched_businesses = []

    return render(request, 'search.html',{'message':message ,'title':title, 'searched_businesses':searched_businesses,'profile':profile})

  else:
    message = 'You haven\'t searched for any business'
    
    title = 'Search Error'
    return render(request,'search.html',{'message':message,'title':title,'profile':profile})

@login_required(login_url='/accounts/login/')
def comments(request):
  user = request.user

  comments = Comment.objects.all()
  return render(request, 'comment.html',{'profile':user,'comments':comments})


@login_required(login_url='/accounts/login/')
def chat(request):
  id = request.user.id
  profile = Profile.objects.get(user=id)


  return render(request, 'chat.html',{'profile':profile})