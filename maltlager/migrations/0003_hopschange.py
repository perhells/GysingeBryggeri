# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maltlager', '0002_maltchange'),
    ]

    operations = [
        migrations.CreateModel(
            name='HopsChange',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField(default=0)),
                ('time', models.TimeField()),
            ],
        ),
    ]
