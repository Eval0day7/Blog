# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-05 14:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期'),
        ),
    ]