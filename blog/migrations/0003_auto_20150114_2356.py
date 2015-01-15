# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Acessos Blog', 'ordering': ['-create_date'], 'verbose_name': 'Acesso Blog'},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, max_length=200, default=datetime.datetime(2015, 1, 14, 23, 56, 43, 361369)),
            preserve_default=False,
        ),
    ]
