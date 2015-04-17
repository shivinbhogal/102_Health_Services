# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0003_speciality_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='slug',
            field=models.SlugField(),
        ),
    ]
