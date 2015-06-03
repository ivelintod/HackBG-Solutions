# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kino', '0005_auto_20150521_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projection',
            name='date',
            field=models.DateField(verbose_name='projection date'),
        ),
        migrations.AlterField(
            model_name='projection',
            name='time',
            field=models.TimeField(verbose_name='time of projection'),
        ),
    ]
