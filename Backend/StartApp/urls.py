"""StartApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from innovations import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal_cabinet/<int:pk>/anketa', views.PersonalCabinetAnketa.as_view()),
    path('personal_cabinet/<int:pk>/profile', views.PersonalCabinetProfile.as_view()),
    path('personal_cabinet/<int:pk>/projects', views.PersonalCabinetProjects.as_view()),
    path('personal_cabinet/<int:pk>/applications', views.PersonalCabinetApplications.as_view()),
    path('img/<string>', views.Img.as_view()),
    path('registration', views.Registration.as_view()),
    path('login', views.Authentification.as_view()),
    path('logout', views.LogOut.as_view()),
    path('confirm/<int:pk>/', views.Confirm.as_view()),
    path('home', views.StartPage.as_view()),
    path('', views.FrontendRenderer.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
