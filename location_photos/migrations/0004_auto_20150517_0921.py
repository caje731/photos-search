# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location_photos', '0003_auto_20150517_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='link',
            field=models.TextField(unique=True),
        ),
    ]
