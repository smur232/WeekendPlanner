# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-08 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_auto_20160204_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]