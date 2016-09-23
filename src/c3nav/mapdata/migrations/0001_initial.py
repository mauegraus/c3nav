# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 15:15
from __future__ import unicode_literals

import c3nav.mapdata.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('name', models.SlugField(help_text='e.g. noc', primary_key=True, serialize=False, verbose_name='feature identifier')),
                ('feature_type', models.CharField(choices=[('building', 'Building'), ('room', 'Room'), ('outside', 'Outside Area'), ('obstacle', 'Obstacle')], max_length=50)),
                ('geometry', c3nav.mapdata.fields.GeometryField()),
            ],
        ),
        migrations.CreateModel(
            name='FeatureTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featuretitles', to='mapdata.Feature', verbose_name='map package')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('name', models.SlugField(help_text='Usually just an integer (e.g. -1, 0, 1, 2)', primary_key=True, serialize=False, verbose_name='level name')),
                ('altitude', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='level altitude')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('name', models.SlugField(help_text='e.g. de.c3nav.33c3.base', primary_key=True, serialize=False, verbose_name='package identifier')),
                ('home_repo', models.URLField(null=True, verbose_name='URL to the home git repository')),
                ('commit_id', models.CharField(max_length=40, null=True, verbose_name='current commit id')),
                ('bottom', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='bottom coordinate')),
                ('left', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='left coordinate')),
                ('top', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='top coordinate')),
                ('right', models.DecimalField(decimal_places=2, max_digits=6, null=True, verbose_name='right coordinate')),
                ('directory', models.CharField(max_length=100, verbose_name='folder name')),
                ('depends', models.ManyToManyField(to='mapdata.Package')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('name', models.SlugField(primary_key=True, serialize=False, verbose_name='source name')),
                ('bottom', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='bottom coordinate')),
                ('left', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='left coordinate')),
                ('top', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='top coordinate')),
                ('right', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='right coordinate')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sources', to='mapdata.Package', verbose_name='map package')),
            ],
        ),
        migrations.AddField(
            model_name='level',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='mapdata.Package', verbose_name='map package'),
        ),
        migrations.AddField(
            model_name='feature',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='mapdata.Level', verbose_name='level'),
        ),
        migrations.AddField(
            model_name='feature',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='mapdata.Package', verbose_name='map package'),
        ),
        migrations.AlterUniqueTogether(
            name='featuretitle',
            unique_together=set([('feature', 'language')]),
        ),
    ]
