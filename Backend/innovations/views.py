from django.shortcuts import render, redirect
from .mail_sender import sender
from . import serializers, models
from rest_framework import generics, response
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

email = ""
code = ""


class personal_cabinet_profile(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        user_session = request.session.get("user")
        user = User.objects.get(nickname=user_session["username"])
        return response.Response({'description': user.description, 'fio': user.fio, 'photo': user.image})

    def post(self, request, *args, **kwargs):
        if request.key == "photo":
            user_session = request.session.get("user")
            user = User.objects.get(nickname=user_session["username"])
            new_url = "127.0.0.1/" + user.id + "/" + request.file.name
            photo = models.photo.objects.get(url=user.image)
            photo.url = new_url
            photo.file = request.file
            user.image = new_url
            photo.save()
            user.save()
            fs = FileSystemStorage
            fs.save(request.file.name, request.file)  ##подписать в регистрации создание объекта таблицы image
            return response.Response({"ok": "yeea"})

        elif request.key == "edit_password":
            pass
        elif request.key == "edit_email":
            pass


class personal_cabinet_anketa(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        user_session = request.session.get("user")
        user = User.objects.get(nickname=user_session["username"])
        return response.Response({'user': user})

    def post(self, request, *args, **kwargs):
        name = request.name
        surname = request.surname
        patronymic = request.patronymic
        fio = surname + "," + name + "," + patronymic
        bornAge = request.date_borned
        country = request.country
        city = request.city
        citizenship = request.citizenship
        sex = request.male
        phone = request.phone
        university = request.university
        speciality = request.speciality
        date_expirated = request.date_expirated
        education = university + speciality + date_expirated
        email = request.email
        busyness = request.employment
        experience = request.work_experience
        skills_mas = request.skills
        skills = ""
        for i in range(skills_mas):
            skills = skills + skills_mas[i] + ","
        achievements = request.achievments
        isTeam = request.is_has_team
        role = request.role
        requisites = request.requisites
        inn = request.inn
        user_session = request.session.get("user")
        user = User.objects.get(nickname=user_session["username"])
        user.fio = fio
        user.bornAge = bornAge
        user.country = country
        user.city = city
        user.citizenship = citizenship
        user.sex = sex
        user.phone = phone
        user.education = education
        user.email = email
        user.busyness = busyness
        user.expirence = experience
        user.skills = skills
        user.achievments = achievements
        user.isTeam = isTeam
        user.role = role
        user.requisites = requisites
        user.inn = inn
        user.save()
        return response.Response({"status": "ok"})


class personal_cabinet_projects(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        projects = models.Projects.objects.get(host=request.session.get("user")["username"])
        projects_mas = []
        for i in range(projects):
            projects_mas[i] = projects[i]
        return response.Response({"projects": projects_mas})

    def post(self, request, *args, **kwargs):
        pass


class personal_cabinet_applications(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        user_session = request.session.get("user")
        user = User.objects.get(username=user_session["username"])
        id_projects = user.applications.split()
        projects = []
        for i in range(id_projects):
            projects[i] = models.Projects.get(id=id_projects[i])
        return response.Response({"projects": projects})

    def post(self, request, *args, **kwargs):
        user_session = request.session.get("user")
        user = User.objects.get(username=user_session["username"])
        id_projects = user.applications.split()
        id_projects.remove(request.project_id)
        projects = []
        projects_bd = ""
        for i in range(id_projects):
            projects[i] = models.Projects.get(id=id_projects[i])
            projects_bd = projects_bd + id_projects[i] + ","
        user.applications = projects_bd
        user.save()
        return response.Response({"projects": projects})


class img(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        return response.Response(models.photo.objects.get(url=(request.build_absolute_uri)).file)


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
            return render(request, "Неправильный код")
