# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-29 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20170928_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='addtime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
