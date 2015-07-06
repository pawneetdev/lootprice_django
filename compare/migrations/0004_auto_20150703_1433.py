# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0003_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='camera',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mobile',
            name='os',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mobile',
            name='processor',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
