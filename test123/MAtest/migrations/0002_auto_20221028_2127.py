# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-10-28 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MAtest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urls',
            old_name='httpurl',
            new_name='http_url',
        ),
    ]
