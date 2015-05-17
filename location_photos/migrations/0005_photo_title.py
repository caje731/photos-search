# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location_photos', '0004_auto_20150517_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]
