# Generated by Django 3.0.5 on 2020-05-11 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteBack', '0005_auto_20200511_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uservote',
            name='userEmail',
            field=models.EmailField(blank=True, default='', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='voteprofile',
            name='voteKey',
            field=models.CharField(blank=True, default='C1GUjTKd', max_length=30),
        ),
    ]