from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request):
    print("hello")
    return render(request, '1.html')