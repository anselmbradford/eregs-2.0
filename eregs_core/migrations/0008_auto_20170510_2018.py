# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eregs_core', '0007_auto_20170510_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regnode',
            old_name='version',
            new_name='reg_version',
        ),
    ]
