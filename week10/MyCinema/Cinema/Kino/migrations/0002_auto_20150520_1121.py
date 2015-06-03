# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kino', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projections',
            name='movie_id',
            field=models.ForeignKey(to='Kino.Movies'),
        ),
    ]
