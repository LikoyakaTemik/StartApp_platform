# Generated by Django 4.1.2 on 2022-10-29 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innovations', '0002_chats_commands_links_projects_remove_ouruser_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ouruser',
            name='bornAge',
            field=models.CharField(default=15, max_length=20),
        ),
    ]