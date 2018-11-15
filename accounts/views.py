from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from . import views


# Create your views here.

def newpage(request):
    time = datetime.datetime.now()
    return render(request,'accounts/newpage.html',{'time':time})

def signup(request):
    time = datetime.datetime.now()
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'Username taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                new = auth.login(request,user)
                return redirect('home')
                #return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return render(request,'accounts/signup.html',{'error':'Passwords must match'})
    else:
        return render(request,'accounts/signup.html',{'time':time})

def login(request):
    time = datetime.datetime.now()
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
            #return HttpResponseRedirect(reverse_lazy('home'))
        else:
            return render(request,'accounts/login.html',{'error':'Username or Password is incorrect!'})
    else:
        return render(request,'accounts/login.html',{'time':time})



def logout(request):
    time = datetime.datetime.now()
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    #return render(request,'accounts/signup.html',{'time':time}) # THIS NEEDS A REVERSE CALL
