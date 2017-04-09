# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0027_albumname_release_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='albumname',
            name='lead_guitar',
            field=models.ManyToManyField(related_name='_albumname_lead_guitar_+', to='album.Shilpi'),
        ),
        migrations.AddField(
            model_name='albumname',
            name='voice',
            field=models.ManyToManyField(related_name='_albumname_voice_+', to='album.Shilpi'),
        ),
        migrations.AlterField(
            model_name='albumname',
            name='release_year',
            field=models.IntegerField(blank=True, default=2016, null=True, verbose_name='\u09ae\u09c1\u0995\u09cd\u09a4\u09bf\u09b0 \u09ac\u099b\u09b0'),
        ),
    ]
