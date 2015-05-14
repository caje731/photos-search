# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location_photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='loc_type',
            field=models.IntegerField(default=2, choices=[(1, b'Restaurant / Eatery'), (2, b'Monument / Tourist Place')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='facebook_id',
            field=models.CharField(max_length=30, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='foursquare_id',
            field=models.CharField(max_length=30, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(null=True, verbose_name=b'latitude', max_digits=10, decimal_places=8),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(null=True, verbose_name=b'longitude', max_digits=10, decimal_places=8),
        ),
    ]
