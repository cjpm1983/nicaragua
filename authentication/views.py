# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from django.contrib.auth.models import User
from usuario.models import UserProfile as User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from django.core.mail import send_mail

from django.contrib.auth import logout as auth_logout


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                msg = "registrado"
                #return render(request, "reservacion/index.html", {"user": user})
                return redirect("/reservar")

            else:    
                msg = 'Credenciales Incorrectas'    
        else:
            msg = 'Error de validacion'    


    return render(request, "authentication/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "authentication/register.html", {"form": form, "msg" : msg, "success" : success })

def logout(request):
    auth_logout(request)
    return redirect("/")

