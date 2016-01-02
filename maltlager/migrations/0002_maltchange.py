# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maltlager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaltChange',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField(default=0)),
                ('time', models.TimeField()),
            ],
        ),
    ]
