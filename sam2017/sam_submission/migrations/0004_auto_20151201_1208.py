# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam_submission', '0003_auto_20151130_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='paper',
            name='is_assigned',
            field=models.BooleanField(default=0),
        ),
    ]
