# Generated by Django 4.1.1 on 2022-12-18 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_professor_establishments_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='groups',
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.group'),
        ),
        migrations.AlterField(
            model_name='department',
            name='establishment',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.establishment'),
        ),
        migrations.AlterField(
            model_name='group',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.group'),
        ),
    ]