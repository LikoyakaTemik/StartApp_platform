# Generated by Django 4.1.2 on 2022-10-29 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innovations', '0006_alter_ouruser_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ouruser',
            name='country',
            field=models.CharField(default='15', max_length=50),
        ),
    ]
