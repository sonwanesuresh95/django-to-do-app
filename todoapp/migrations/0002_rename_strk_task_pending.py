# Generated by Django 3.2.4 on 2021-06-27 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='strk',
            new_name='pending',
        ),
    ]
