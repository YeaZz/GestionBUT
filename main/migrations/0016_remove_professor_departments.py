# Generated by Django 4.1.1 on 2022-12-20 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_competence_ue_remove_resource_department_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='departments',
        ),
    ]