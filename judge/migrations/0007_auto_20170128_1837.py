# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-28 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0006_auto_20170128_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='id',
        ),
        migrations.AlterField(
            model_name='problem',
            name='pcode',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]