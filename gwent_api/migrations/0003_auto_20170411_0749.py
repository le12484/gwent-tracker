# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 07:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gwent_api', '0002_card_art'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='variations',
        ),
        migrations.AddField(
            model_name='card',
            name='availability',
            field=models.ForeignKey(default='BaseSet', on_delete=django.db.models.deletion.CASCADE, to='gwent_api.CardSet'),
            preserve_default=False,
        ),
    ]