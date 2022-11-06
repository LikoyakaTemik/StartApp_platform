from django.db import models
def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class photo(models.Model):
    pass


class Projects(models.Model):
    pass


class email_confirm(models.Model):
    email = models.EmailField()
    url = models.URLField()