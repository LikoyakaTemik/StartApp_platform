# Generated by Django 4.1.2 on 2022-10-29 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('innovations', '0007_alter_ouruser_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ouruser',
            name='description',
            field=models.CharField(default='15', max_length=10000),
        ),
    ]
