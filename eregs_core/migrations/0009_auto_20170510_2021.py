# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 20:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eregs_core', '0008_auto_20170510_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diffnode',
            name='left_version',
        ),
        migrations.RemoveField(
            model_name='diffnode',
            name='right_version',
        ),
    ]
