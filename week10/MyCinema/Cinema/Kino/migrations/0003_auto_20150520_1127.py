# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kino', '0002_auto_20150520_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
        migrations.RenameModel(
            old_name='Projections',
            new_name='Projection',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='projection_id',
        ),
        migrations.DeleteModel(
            name='Reservations',
        ),
        migrations.AddField(
            model_name='reservation',
            name='projection_id',
            field=models.ForeignKey(to='Kino.Projection'),
        ),
    ]
