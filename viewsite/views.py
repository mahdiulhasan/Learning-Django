from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    time = datetime.now()
    return HttpResponse("<h2>Hello from Django: {}</h2>".format(time))