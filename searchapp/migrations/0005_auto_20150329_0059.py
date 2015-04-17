# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0004_auto_20150329_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
