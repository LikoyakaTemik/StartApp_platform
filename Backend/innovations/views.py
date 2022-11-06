from django.shortcuts import render, redirect
from .mail_sender import sender
from . import serializers, models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.hashers import *
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, response
from rest_framework.views import APIView
from .models import email_confirm
from random import randint
from django.views import View


email = ""
code = ""


def gerenator():
    code = ""
    for i in range(10):
        code = code + str(randint(0, 9))

    try:
        email_confirm.objects.get(url="127.0.0.1/registration/" + code)
        gerenator()
    except:
        return code


class FrontendRenderer(View):
    def get(self, request, *args, **kwargs):
        return render(request, "innovations/main.html", {})


class PersonalCabinetProfile(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
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


class PersonalCabinetAnketa(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
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


class PersonalCabinetProjects(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        projects = models.Projects.objects.get(host=request.session.get("user")["username"])
        projects_mas = []
        for i in range(projects):
            projects_mas[i] = projects[i]
        return response.Response({"projects": projects_mas})

    def post(self, request, *args, **kwargs):
        pass


class PersonalCabinetApplications(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
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


class Img(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        return response.Response(models.photo.objects.get(url=(request.build_absolute_uri)).file)



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


class LogOut(APIView):
    def get(self, request, *args, **kwargs):
        logout(request)
        if request.session.get('user') is not None:
            del request.session["user"]
        return response.Response({'succes': True})



class Registration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    def post(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        user_data = user_serializer.data
        request.session.set_expiry(3600)
        request.session['user'] = user_data

        # email = email_confirm.objects.create(email=user.email)
        # email.url = "127.0.0.1/registration/" + gerenator()
        # email.save()
        # sender(email.email, email.url)
        return response.Response({"username": user.username})


class Confirm(generics.CreateAPIView, generics.RetrieveAPIView, generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        email = email_confirm.objects.get(url=request.build_absolute_uri()).email
        user = User.objects.get(email=email)
        user.is_activated = True
        user.save()
        return response.Response({'post': user.data})


class Authentification(generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        login_text = request.data.get("login")
        password = request.data.get("password")
        try:
            user = User.objects.get(username=login_text)
            user_sender = user
            if check_password(password, user.password):
                user = authenticate(request, username=user.username, password=password)
                login(request, user)
                print(request.user.is_authenticated)
                request.session['user'] = serializers.UserSerializer(instance=user).data
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
        return response.Response({"request": request})

    def get(self, request, *args, **kwargs):
        return response.Response({"is_ok": "ok"})

