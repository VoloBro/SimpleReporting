# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='n/a', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TestRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_id', models.CharField(default='0', max_length=100)),
                ('datetime', models.DateTimeField()),
                ('status', models.CharField(default='n/a', max_length=20)),
                ('messages', models.CharField(default='n/a', max_length=500)),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runscompare.TestCase')),
            ],
        ),
    ]
