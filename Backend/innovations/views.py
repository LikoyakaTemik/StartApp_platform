from django.shortcuts import render
import mail_sender
# Create your views here.

email = []
def menu(request):
    if request.method == "GET":
        return render(request, menu())
    elif request.method == "POST":
        return render(request, "registr.html")


def register(request):
    if request.method == "POST":
        login = request.get.POST("login")
        password = request.get.POST("pass")
        email = [request.get.POST("email")]
        print(login)
        print((password))
        print(email)
        return render(request, "confirm.html")
    elif request.method == "GET":
        return render(request, "registr.html")

def confirm(request):
    code = mail_sender.sender(email[0])

    if request.method == "GET":
        return render(request, "confirm.html")
    elif request.method == "POST":
        if code == request.get.POST("code"):
            return render(request, "Вы зарегистрированы")
        else:
            return render(request,"Неправильный код")