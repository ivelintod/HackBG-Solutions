# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Projections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('movie_id', models.IntegerField()),
                ('movie_type', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='projection date')),
                ('time', models.DateTimeField(verbose_name='time of projection')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('username', models.CharField(max_length=200)),
                ('row', models.IntegerField()),
                ('col', models.IntegerField()),
                ('projection_id', models.ForeignKey(to='Kino.Projections')),
            ],
        ),
    ]
