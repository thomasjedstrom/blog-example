# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]