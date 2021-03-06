# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20171130_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='industries',
            field=models.ManyToManyField(to='api.Industry'),
        ),
    ]
