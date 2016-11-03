# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-03 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petitions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petition',
            name='published',
        ),
        migrations.AddField(
            model_name='petition',
            name='status',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
