from django.urls import path
from.import views

urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('profile/', views.profile, name='profile')
]