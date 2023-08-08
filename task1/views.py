from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello! This is Archanaben Kaushalkumar Patel. My Student ID is s2271787.")
