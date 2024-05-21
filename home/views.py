from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def to_home(request):
    template = loader.get_template('home/home.html')
    return HttpResponse(template.render())