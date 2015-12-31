# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0001_initial'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='result',
        #     name='score',
        #     field=models.Field(blank=True, null=True),
        # ),
        migrations.AlterField(
            model_name='competition',
            name='event_time',
            field=models.TimeField(default='08:00'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='numberOfParticipants',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='personalNotes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='place',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='competition',
            name='result',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='sport.Result'),
        ),
    ]
