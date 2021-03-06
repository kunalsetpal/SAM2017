# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sam_submission', '0004_auto_20151201_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='is_assigned_to',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
