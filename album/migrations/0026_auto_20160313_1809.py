# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0025_auto_20160313_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumname',
            name='album_no',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='\u098f\u09b2\u09ac\u09be\u09ae \u09a8\u09be\u09ae\u09cd\u09ac\u09be\u09b0'),
        ),
    ]
