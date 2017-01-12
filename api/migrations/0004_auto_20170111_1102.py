# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170111_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='password',
            field=models.CharField(max_length=24, default=None, null=True, blank=True),
        ),
    ]
