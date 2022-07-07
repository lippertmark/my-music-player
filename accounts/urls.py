from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('sign_up/', views.user_register, name='sign_up'),
]