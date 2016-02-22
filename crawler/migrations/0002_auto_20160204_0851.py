# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='image',
            new_name='image_url',
        ),
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(default='', max_length=300),
        ),
    ]
