# Generated by Django 3.0.5 on 2020-04-17 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='house_id',
        ),
        migrations.AddField(
            model_name='room',
            name='house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.House'),
        ),
    ]
