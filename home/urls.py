from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.to_home, name='home')
]
