#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, I am Dilisha Shrestha. This is My First Django Project")