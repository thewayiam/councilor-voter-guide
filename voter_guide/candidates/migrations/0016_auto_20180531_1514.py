# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-31 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0015_auto_20180531_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intent',
            name='motivation',
            field=models.TextField(blank=True, null=True, verbose_name='\u70ba\u4f55\u53c3\u9078'),
        ),
    ]
