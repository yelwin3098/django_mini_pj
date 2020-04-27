from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    dict={
        'title':"Home Page"
    }
    return render(request,"page/home.html",dict)

def about(request):
    return HttpResponse("About Page")

def single(request):
    return HttpResponse("Sing Page")