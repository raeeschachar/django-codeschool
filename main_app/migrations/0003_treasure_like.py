# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_treasure_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='treasure',
            name='like',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
