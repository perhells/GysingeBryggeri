# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maltlager', '0003_hopschange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maltchange',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
