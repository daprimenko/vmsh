# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-27 08:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180827_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutpost',
            name='author',
        ),
    ]
