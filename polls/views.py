from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Home Page")


def about(request):
    return HttpResponse("About Page")


def login(request):
    return HttpResponse("Login Page")


def dashboard(request):
    return HttpResponse("Dashboard Page")
