from django.db import models
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)
# Create your models here.

class photo(models.Model):
    pass

class Projects(models.Model):
    pass