# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_provider_moderation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provider',
            options={'ordering': ['name'], 'verbose_name': 'provedor', 'verbose_name_plural': 'provedores'},
        ),
        migrations.AddField(
            model_name='provider',
            name='moderation_comments',
            field=models.TextField(blank=True, verbose_name='Comentários da moderação'),
        ),
        migrations.AddField(
            model_name='provider',
            name='moderation_reason',
            field=models.CharField(choices=[('', 'Não se aplica'), ('R', 'Provedor repetido'), ('N', 'Fonte não encontrada (404)'), ('I', 'Fonte com informações imprecisas ou erradas'), ('A', 'Fonte não acessível (ex.: requer login)'), ('P', 'Fonte é comunicação privada (ex.: chat ou suporte)'), ('O', 'Outros')], default='', max_length=1, verbose_name='Motivo da moderação'),
        ),
    ]
