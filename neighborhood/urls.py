from django.urls import path
from.import views

urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('profile/', views.profile, name='profile'),
    path('businesses/', views.business, name='businesses'),
    path('services/', views.services, name='services'),
    path('posts/', views.posts, name='posts'),
    path('change/', views.change_hood, name='change_hood'),

]