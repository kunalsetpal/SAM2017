# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam_submission', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='is_requested',
            field=models.BooleanField(default=0),
        ),
    ]
