# Generated by Django 4.1.2 on 2022-10-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(default='Stas')),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]