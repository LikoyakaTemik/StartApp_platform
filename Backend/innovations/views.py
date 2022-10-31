from django.shortcuts import render, redirect
from .mail_sender import sender
from . import serializers
from rest_framework import generics, response
from django.contrib.auth.models import User

email = ""
code = ""

class personal_cabinet(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        user_session = request.session.get("user")
        user = User.objects.get(nickname = user_session["nickname"])

    def post(self, request, *args, **kwargs):
        pass


def menu(request):
    if request.method == "GET":
        return render(request, "menu.html")
    elif request.method == "POST":
        return redirect('http://127.0.0.1:8000/registration')


def register(request):
    global email
    global code
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("pass")
        email = request.POST.get("email")
        print(login)
        print(password)
        print(email)
        code = sender(email)
        return redirect('http://127.0.0.1:8000/confirm')
    elif request.method == "GET":
        return render(request, "registr.html")

def confirm(request):
    if request.method == "GET":
        return render(request, "confirm.html")
    elif request.method == "POST":
        print(code)
        if code == request.POST.get("code"):
            return render(request, "Вы зарегистрированы")
        else:
            return render(request,"Неправильный код")