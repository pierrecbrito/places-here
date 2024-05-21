from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.to_login, name="to_login"),
]