# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 00:27
from __future__ import unicode_literals

import c3nav.mapdata.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('editor', '0004_auto_20170620_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangedObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='last update')),
                ('existing_object_pk', models.PositiveIntegerField(null=True, verbose_name='id of existing object')),
                ('updated_fields', c3nav.mapdata.fields.JSONField(default={}, verbose_name='updated fields')),
                ('m2m_added', c3nav.mapdata.fields.JSONField(default={}, verbose_name='added m2m values')),
                ('m2m_removed', c3nav.mapdata.fields.JSONField(default={}, verbose_name='removed m2m values')),
                ('deleted', models.BooleanField(default=False, verbose_name='new field value')),
                ('changeset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='changed_objects_set', to='editor.ChangeSet', verbose_name='Change Set')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='changed_objects_set', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Changed object',
                'verbose_name_plural': 'Changed objects',
                'ordering': ['created', 'pk'],
                'default_related_name': 'changed_objects_set',
            },
        ),
        migrations.RemoveField(
            model_name='change',
            name='author',
        ),
        migrations.RemoveField(
            model_name='change',
            name='changeset',
        ),
        migrations.RemoveField(
            model_name='change',
            name='created_object',
        ),
        migrations.RemoveField(
            model_name='change',
            name='discarded_by',
        ),
        migrations.DeleteModel(
            name='Change',
        ),
        migrations.AlterUniqueTogether(
            name='changedobject',
            unique_together=set([('changeset', 'content_type', 'existing_object_pk')]),
        ),
    ]
