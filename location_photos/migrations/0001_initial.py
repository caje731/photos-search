# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('lat', models.DecimalField(null=True, verbose_name=b'latitude', max_digits=10, decimal_places=8, blank=True)),
                ('lng', models.DecimalField(null=True, verbose_name=b'longitude', max_digits=10, decimal_places=8, blank=True)),
                ('facebook_id', models.CharField(max_length=30, unique=True, null=True, blank=True)),
                ('foursquare_id', models.CharField(max_length=30, unique=True, null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.TextField()),
                ('attribution', models.TextField(blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(related_query_name=b'photo', related_name='photos', to='location_photos.Location')),
            ],
        ),
    ]
