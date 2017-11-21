# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treasure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('material', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(default=b'media/default.png', upload_to=b'treasure_images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
