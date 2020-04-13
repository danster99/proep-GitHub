# Generated by Django 3.0.5 on 2020-04-09 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400)),
                ('max_nr_tenants', models.IntegerField()),
                ('rules', models.CharField(max_length=50000)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(max_length=50)),
                ('is_bookable', models.BooleanField(default=True)),
                ('house_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='houses.House')),
            ],
        ),
    ]
