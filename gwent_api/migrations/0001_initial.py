# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 07:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('flavor', models.TextField(max_length=1200)),
                ('info', models.TextField(max_length=1200)),
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CardSet',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rarity',
            fields=[
                ('name', models.CharField(max_length=120, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwent_api.CardSet')),
                ('rarity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwent_api.Rarity')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='categories',
            field=models.ManyToManyField(to='gwent_api.Category'),
        ),
        migrations.AddField(
            model_name='card',
            name='faction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwent_api.Faction'),
        ),
        migrations.AddField(
            model_name='card',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwent_api.Group'),
        ),
        migrations.AddField(
            model_name='card',
            name='positions',
            field=models.ManyToManyField(to='gwent_api.Position'),
        ),
        migrations.AddField(
            model_name='card',
            name='rarity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gwent_api.Rarity'),
        ),
        migrations.AddField(
            model_name='card',
            name='variations',
            field=models.ManyToManyField(to='gwent_api.Variation'),
        ),
    ]
