from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def to_login(request):
    template = loader.get_template('auth/login.html')
    return HttpResponse(template.render())