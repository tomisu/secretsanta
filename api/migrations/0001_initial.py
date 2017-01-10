# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('is_locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('is_closed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='room',
            field=models.ForeignKey(to='api.Room', related_name='participants'),
        ),
        migrations.AddField(
            model_name='entry',
            name='giftee',
            field=models.ForeignKey(to='api.Participant', related_name='giftee_entries'),
        ),
        migrations.AddField(
            model_name='entry',
            name='gifter',
            field=models.ForeignKey(to='api.Participant', related_name='gifter_entries'),
        ),
        migrations.AddField(
            model_name='entry',
            name='room',
            field=models.ForeignKey(to='api.Room', related_name='entries'),
        ),
    ]
