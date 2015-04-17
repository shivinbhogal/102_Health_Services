# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0005_auto_20150329_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='slug',
            field=models.SlugField(),
        ),
    ]
