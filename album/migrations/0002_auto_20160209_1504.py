# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 09:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lirisist',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='lirisist',
            name='email',
        ),
        migrations.RemoveField(
            model_name='lirisist',
            name='last_name',
        ),
    ]
