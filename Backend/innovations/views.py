from django.shortcuts import render, redirect
from .mail_sender import sender
from django.contrib.auth.models import User
from django.contrib.auth.hashers import *
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, response
from . import serializers
from models import email_confirm
import random

email = ""
code = ""

def gerenator():
    code = ""
    for i in range(10):
        code = code + random(0, 9)

    try:
        email_confirm.objects.get(url="127.0.0.1/registration/" + code)
        gerenator()
    except:
        return code


class StartPage(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        try:
            user = request.session.get('user')
            user_sender = user
            password_encoded = (User.objects.get(username=user["username"])).password
            password = user['password']
            if check_password(password, password_encoded):
                user = authenticate(request, username=user['username'], password=password)
                login(request, user)
                print(request.user.is_authenticated)

            return response.Response({"username": user_sender.username})
        except:
            return response.Response({'username': 'AnonUser'})


class LogOut(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        logout(request)
        request.session['user'].delete()
        return response.Response({'succes': True})

def menu(request):
    if request.method == "GET":
        try:
            user = request.session.get('user')
            print(request.session.get('user'))
            password_encoded = (User.objects.get(username=user["login"])).password
            password = user['password']
            
            if check_password(password, password_encoded):
                user = authenticate(request, username=user['login'], password=password)
                login(request, user)
                print(request.user.is_authenticated)
            return render(request, "menu.html")
        except:
            return render(request, "menu.html")

    elif request.method == "POST":
        if request.POST.get("auth") == "Выйти":
            logout(request)
            return redirect("http://127.0.0.1:8000")
        elif request.POST.get("auth") == "Регистрация":
            return redirect('http://127.0.0.1:8000/registration')



class Registration(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def post(self, request, *args, **kwargs):
        quaryset = User.objects.all()
        serializers_class = serializers.UserSerializer
        user = self.get_serializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        request.session.set_expiry(3600)
        request.session['user'] = user

        email = email_confirm.objects.create(email=user.email)
        email.url = "127.0.0.1/registration/" + gerenator()
        email.save()
        sender(email.email, email.url)
        return response.Response({'send': True})

class Confirm(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        email = email_confirm.objects.get(url=request.build_absolute_uri()).email
        user = User.objects.get(email=email)
        user.is_activated = True
        user.save()
        return response.Response({'post': user.data})

def register(request):
    global email
    global code
    if request.method == "POST":

        login = request.POST.get("login")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(login, email, password)
        user.last_name = "Bukich"
        user.save()
        request.session.set_expiry(3600)
        request.session['user'] = request.POST
        print("-------------------------------")
        return redirect('http://127.0.0.1:8000')
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
            return render(request, "Неправильный код")

class Authentification(generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        login = request.POST.get("login")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=login)
            user_sender = user
            if check_password(password, user.password):
                user = authenticate(request, username=user['login'], password=password)
                login(request, user)
                print(request.user.is_authenticated)
                request.session['user'] = user_sender
                return response.Response({'username': user.username})
            else:
                return response.Response({'username': 'AnonUser'})
        except:
            try:
                user = User.objects.get(email=login)
                user_sender = user
                if check_password(password, user.password):
                    user = authenticate(request, username=user['login'], password=password)
                    login(request, user)
                    print(request.user.is_authenticated)
                    request.session['user'] = user_sender
                    return response.Response({'username': user.username})
                else:
                    return response.Response({'username': 'AnonUser'})
            except:
                return response.Response({'username': 'AnonUser'})

def authentificate(request):
    if request.method == "GET":
        if request.session["user_id"] == -999:
            print("isn't authentificate")
        else:
            print("authentificated")
        return render(request, "confirm.html")
    elif request.method == "POST":
        #request.session["user_id"] = user.objects.get(id == 3, -999)
        request.session.modified = True
        return render(request, "confirm.html")

class Questionnaire(generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        list_of_date = []
        FIO = request.POST.get("FIO")
        list_of_date.append(FIO)
        date_of_birth = request.POST.get("date_of_birth")
        list_of_date.append(date_of_birth)
        country = request.POST.get("country")
        list_of_date.append(country)
        town = request.POST.get("town")
        list_of_date.append(town)
        citizenship = request.POST.get("сitizenship")
        list_of_date.append(citizenship)
        sex = request.POST.get("sex")
        list_of_date.append(sex)
        phonenumber = request.POST.get("phonenumber")
        list_of_date.append(phonenumber)
        education = request.POST.get("education")
        list_of_date.append(education)
        employment = request.POST.get("employment")
        list_of_date.append(employment)
        work_experience = request.POST.get("work_experience")
        list_of_date.append(work_experience)
        skills = request.POST.get("skills")
        list_of_date.append(skills)
        achievements = request.POST.get("achievements")
        list_of_date.append(achievements)
        team = request.POST.get("team")
        list_of_date.append(team)
        role_in_team = request.POST.get("role_in_team")
        list_of_date.append(role_in_team)
        is_confirmed = True
        for obj in list_of_date:
            if obj is None:
                is_confirmed = False

        is_author = request.POST.get("is_author")
        doc_of_author = request.POST.get("doc_of_author")
        if is_author == True:
            if doc_of_author is None:
                is_confirmed = False
        is_company = request.POST.get("is_company")
        INN = request.POST.get("INN")
        if is_company == True:
            if INN is None:
                is_confirmed = False
        user = User.objects.get(username=request.session["user"]['username'])
        return response.Response(request)

    def get(self, request, *args, **kwargs):
        return response.Response(request)
