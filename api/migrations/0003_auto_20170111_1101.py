# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_entry_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='password',
            field=models.CharField(default=None, null=True, max_length=24),
        ),
    ]
