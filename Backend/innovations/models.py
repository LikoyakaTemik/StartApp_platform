from django.db import models

# Create your models here.
class email_confirm(models.Model):
    email = models.EmailField()
    url = models.URLField()