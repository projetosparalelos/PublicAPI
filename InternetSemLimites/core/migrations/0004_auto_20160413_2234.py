# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 01:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20160413_2209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provider',
            options={'ordering': ['name'], 'verbose_name': 'Provedor', 'verbose_name_plural': 'Provedores'},
        ),
    ]
