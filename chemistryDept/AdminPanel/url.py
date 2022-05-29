from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminPanel, name='AdminPanel'),
    path('Adminprofile/', views.Adminprofile, name='Adminprofile'),
    path('blank/', views.blank, name='blank'),
]