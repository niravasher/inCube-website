# Generated by Django 2.0 on 2018-07-23 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_project_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='files',
        ),
    ]
