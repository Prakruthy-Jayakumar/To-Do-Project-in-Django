# Generated by Django 3.2.12 on 2022-02-18 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0002_task_date_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date_task',
            new_name='date',
        ),
    ]
