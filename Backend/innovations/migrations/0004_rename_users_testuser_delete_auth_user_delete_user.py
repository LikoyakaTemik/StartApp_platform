# Generated by Django 4.1.2 on 2022-10-22 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('innovations', '0003_auth_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='TestUser',
        ),
        migrations.DeleteModel(
            name='auth_user',
        ),
        migrations.DeleteModel(
            name='user',
        ),
    ]
