# Generated by Django 3.0.5 on 2020-04-17 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilities', '0002_auto_20200417_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utility',
            name='is_bookable',
        ),
    ]
