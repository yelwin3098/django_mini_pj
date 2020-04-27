from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.models import User

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data.get("username")
            messages.success(request,f'Register Success with name of {name}')
            return redirect('home-page')
    else:
        form=UserCreationForm()
    dict={
        "title":"User Register Page",
        'form':form
    }
    return render(request,'user/register.html',dict)  

@login_required
def profile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Update Success')
            return redirect('user-profile-page')
    else:
        username=request.user.username
        p_form= ProfileUpdateForm(instance=request.user.profile)
        u_form=UserUpdateForm(instance=request.user)

    dict={
        "title":f"{username} Profile Page",
        'p_form':p_form,
        'u_form':u_form
    }
    return render(request,'user/profile.html',dict)
