# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-27 06:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutpost',
            options={'verbose_name': 'описание сайта', 'verbose_name_plural': 'описание сайта'},
        ),
    ]
