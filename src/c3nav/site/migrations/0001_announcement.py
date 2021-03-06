# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 22:51
from __future__ import unicode_literals

import c3nav.mapdata.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('active_until', models.DateTimeField(null=True, verbose_name='active until')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('message', c3nav.mapdata.fields.I18nField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'Announcements',
                'get_latest_by': 'created',
                'default_related_name': 'announcements',
            },
        ),
    ]
