from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from hello.models import login
from hello.forms import *


def loginPage(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        form.save()

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse('<h1>done</h1>')

        else:
            messages.info(request,'Username or password is incorrect')
            

    context={}
    return render(request,'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    form=CreateUserForm()

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was successfully created for '+ user)
            return redirect('login')

    context={'form':form}
    return render(request,"register.html", context)
