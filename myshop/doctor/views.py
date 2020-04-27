from django.shortcuts import render,redirect
from .forms import CategoryCreateForm,DoctorCreateForm
from django.contrib import messages
from .models import Category,Doctor

def home(request):
    cats=Category.objects.all()
    dict={
        "title":"Find A Doctor",
        "cats":cats
    }    
    return render(request,"doctor/home.html",dict)

def showDoctors(request):
    docts=Doctor.objects.all()
    dict={
        "title":"Find A Doctor",
        "docts":docts
    }    
    return render(request,"doctor/show_doctors.html",dict)


def createCat(request):
    if request.method=="POST":
        form=CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Category Created!")
            return redirect('doctor-home-page')
    else:
        form=CategoryCreateForm()
        cats=Category.objects.all()
    dict={
        "title":"Create Category",
        "form":form,
        "cats":cats
    }    
    return render(request,"doctor/catcreate.html",dict)

def createDoctor(request):
    if request.method=="POST":
        form=DoctorCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Doctor Created!")
            return redirect('doctor-show-page')
    else:
        form=DoctorCreateForm()

    dict={
        "title":"Doctor Create Page",
        "form":form,
    }    
    return render(request,"doctor/doctor_create.html",dict)

def filterDoctors(request,pk):
    docts=Doctor.objects.filter(category=pk)
    dict={
        "title":"Doctor Show Page",
        "docts":docts,
    }    
    return render(request,"doctor/show_doctors.html",dict)    