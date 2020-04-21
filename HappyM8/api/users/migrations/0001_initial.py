# Generated by Django 3.0.5 on 2020-04-21 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_nr', models.CharField(blank=True, max_length=30, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(1, 'pending'), (2, 'assigned'), (3, 'unassigned')], default=1, max_length=15)),
                ('code', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='houses.House')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
