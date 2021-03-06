# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayOfWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.IntegerField(choices=[(1, 'Понедельник'), (2, 'Вторник'), (3, 'Среда'), (4, 'Четверг'), (5, 'Пятница'), (6, 'Суббота')], unique=True, verbose_name='день недели')),
            ],
            options={
                'verbose_name': 'день недели',
                'verbose_name_plural': 'дни недели',
                'ordering': ['day'],
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='класс')),
            ],
            options={
                'verbose_name': 'класс',
                'verbose_name_plural': 'классы',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='название')),
                ('room', models.CharField(max_length=10, verbose_name='аудитория')),
                ('time', models.TimeField(verbose_name='время')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.DayOfWeek', verbose_name='день недели')),
                ('grade', models.ManyToManyField(to='diary.Grade', verbose_name='класс')),
            ],
            options={
                'verbose_name': 'предмет',
                'verbose_name_plural': 'предметы',
                'ordering': ['name'],
            },
        ),
    ]
