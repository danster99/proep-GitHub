# Generated by Django 3.0.5 on 2020-04-17 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chore',
            old_name='beginTime',
            new_name='begin_time',
        ),
        migrations.RenameField(
            model_name='chore',
            old_name='endTime',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='chore',
            old_name='userId',
            new_name='user',
        ),
    ]
