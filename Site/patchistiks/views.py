from pickle import NONE
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone

from .models import *

def home(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        user=authenticate(request,username=username, password=password)
        context={'user':user}
        if user is not None:
            login(request,user)
            return render(request, 'patchistiks/home.html', context)
        else:
            return render(request, 'patchistiks/home.html',context)
    return render(request, 'patchistiks/home.html')

def my_logout(request):
    logout(request)
    return render(request, 'patchistiks/home.html')
    
def profile(request):
    championList = []
    for list_champ in Champions.objects.all():
        for user_champ in list_champ.pick.all():
            if user_champ == request.user:
                championList.append(list_champ)
    context = {'champList': championList}
    return render(request, 'patchistiks/profil.html', context)

def myLogin(request):
    return render(request,'patchistiks/login.html')

def register(request):
    return render(request, 'patchistiks/register.html')