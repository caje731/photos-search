# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location_photos', '0002_auto_20150512_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='bytes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='width',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='loc_type',
            field=models.IntegerField(default=2, verbose_name=b'Type', choices=[(1, b'Restaurant / Eatery'), (2, b'Monument / Tourist Place')]),
        ),
    ]
