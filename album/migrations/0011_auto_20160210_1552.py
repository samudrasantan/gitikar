# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0010_auto_20160210_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='members',
        ),
        migrations.DeleteModel(
            name='Band',
        ),
    ]
