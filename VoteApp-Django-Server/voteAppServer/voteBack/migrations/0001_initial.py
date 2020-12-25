# Generated by Django 3.0.5 on 2020-04-08 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30, unique=True)),
                ('passWord', models.CharField(max_length=50)),
                ('userEmail', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('userPhone', models.CharField(blank=True, default='', max_length=13, unique=True)),
                ('gender', models.NullBooleanField()),
                ('birth', models.DateField(auto_now_add=True)),
                ('education', models.CharField(blank=True, default='', max_length=50)),
                ('regDate', models.DateField(auto_now_add=True)),
            ],
        ),
    ]