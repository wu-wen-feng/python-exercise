# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-28 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='This is a title', max_length=12)),
                ('content', models.TextField(null=True)),
            ],
        ),
    ]
