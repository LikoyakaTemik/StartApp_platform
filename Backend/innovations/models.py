from django.db import models
from django.contrib.auth.models import User, AbstractUser
#from django.contrib.postgres.fields import ArrayField

# Create your models here.
class OurUser(AbstractUser):
    fio = models.CharField(max_length=200, default="15")
    bornAge = models.CharField(max_length=20, default=15)
    country = models.CharField(max_length=50, default="15")
    city = models.CharField(max_length=200, default="15")
    citizenship = models.CharField(max_length=200, default="15")
    sex = models.BooleanField(default=0)
    phone = models.CharField(max_length=30, default="15")
    education = models.CharField(max_length=200, default="15")
    busyness = models.CharField(max_length=200, default="15")
    experience = models.IntegerField(default=-1)
    skills = models.CharField(max_length=1000, default="15")
    jopa = models.CharField(max_length=1000, default="15")
    isTeam = models.BooleanField(default=0)
    role = models.CharField(max_length=100, default="15")
    isAuthor = models.CharField(max_length=100, default="15")
    requisites = models.CharField(max_length=100, default="15")
    isCompany = models.CharField(max_length=100, default="15")
    inn = models.CharField(max_length=100, default="15")
    image = models.ImageField(upload_to=None, default="15")
    description = models.CharField(max_length=10000, default="15")
    project_likes = models.CharField(max_length=10000, default="15")
    isForm = models.BooleanField(default=0)
    isActivated = models.BooleanField(default=0)

class Links(models.Model):
    email = models.CharField(max_length=300, default=None)
    link = models.CharField(max_length=300, default=None)

class Projects(models.Model):
    title = models.CharField(max_length=100, default=None)
    little_description = models.CharField(max_length=500, default=None)
    main_description = models.CharField(max_length=50000, default=None)
    documents = models.FileField(upload_to=None)
    host = models.CharField(max_length=100, default=None)
    skills = models.CharField(max_length=300, default=None)
    likes = models.IntegerField(default=-1)
    link = models.URLField(max_length=300, default=None)
    date_of_public = models.DateTimeField(default=None)
    id_of_command_developments = models.IntegerField(default=-1)
    applications = models.CharField(max_length=10000, default=None)

class Commands(models.Model):
    participant = models.CharField(max_length=10000, default=None)
    chat_id = models.IntegerField(default=-1)

class Chats(models.Model):
    email = models.CharField(max_length=10000, default=None)
'''
Необходимые поля 1.Таблицы юзеров(которую необходимо наследовать):
1.1 Логин;(есть в изначальной)
1.2. Пароль(есть в изначальной)
1.3. email(есть в изначальной)
1.4. ФИО
1.5. Дата рождения
1.6. Страна
1.7. Город
1.8. Гражданство
1.9. Пол
1.10. Телефон
1.11. Образование(ВУЗ, специальность, год окончания)
1.12. Занятость
1.13. Опыт работы(лет)
1.14. Навыки
1.15. Достижения/проф. опыт
1.16. Наличие команды(команда проекта)
1.17. роль в команде
1.18. Является ли автором объектов интеллектуальной собственности (есть ли патент)? Если да, то запрос реквизитов документа.
1.19. Реквизиты документа(по ум. None)
1.20. Есть ли своя компания? Если да, то запрос ИНН.
1.21. ИНН(по ум. None)
1.22. поле фотографии
1.23. Описание пользователя
1.24 массив id-шников лайкнутых юзером проектов
1.25 Заполнена ли анкета?(True или False)
1.26 is_activated(Активирован ли аккаунт(по почте), True или False)
2. Таблица ссылок подтверждения почт юзеров(при регистрации на почту будет высылаться ссылка, при переходе на которую юзер будет подтверждать её и соответственно регистрироваться):
2.1. email
2.2. индивидуальная ссылка
3. Таблица проектов:
3.1 Загаловок/Название
3.2. КРАТКОЕ описание
3.3 Основное описание
3.4 Приложения(возможно, какие-то фотографии)
3.5 Владелец проекта
3.6 Необходимые навыки разработчиков для реализации
3.7 количество лайков проекта другими пользователями
3.8 индив. ссылка на проект
3.9 дата публикации
3.10 id привязанной к нему команды разработчиков
3.11 Список заявок на участие(может быть массив из id-шников кандидатов)
4. Таблица команд:
4.1 Массив из id-шников членов команд
4.2 id чата проекта
5. Таблица чатов:
5.1 Сообщение(Массив из словарей вида: {username: 123, message: 123, date: [25.10.22, 0:45])}
'''