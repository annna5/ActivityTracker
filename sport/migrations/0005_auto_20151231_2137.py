# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 20:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0004_auto_20151231_2124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='result',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]
