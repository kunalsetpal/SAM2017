# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam_submission', '0012_auto_20151202_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='counter',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='is_assigned',
        ),
    ]
