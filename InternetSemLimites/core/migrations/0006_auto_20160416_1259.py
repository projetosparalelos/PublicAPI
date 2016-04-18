# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 15:59
from __future__ import unicode_literals

from django.db import migrations

PUBLISHED = 'P'
NEW = 'N'


def set_status(apps, schema_editor):
    Provider = apps.get_model('core', 'Provider')
    for provider in Provider.objects.all():
        if provider.published:
            provider.status = PUBLISHED
        else:
            provider.status = NEW
        provider.save()


def set_published(apps, schema_editor):
    Provider = apps.get_model('core', 'Provider')
    for provider in Provider.objects.all():
        if provider.status == Provider.PUBLISHED:
            provider.published = True
        else:
            provider.published = False
        provider.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_provider_status'),
    ]

    operations = [
        migrations.RunPython(set_status, set_published),
    ]