# Generated by Django 4.1.3 on 2022-11-25 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ManyToManyField(to='main.group'),
        ),
    ]
