# Generated by Django 4.1.1 on 2023-01-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_course_buts_remove_year_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='note',
            field=models.FloatField(default=0),
        ),
    ]
