# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2022-08-07 02:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='teacher',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='exp',
            field=models.FloatField(default=0),
        ),
    ]
