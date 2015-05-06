# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='header_desc',
            field=models.TextField(default=b'Short description', max_length=200),
        ),
        migrations.AddField(
            model_name='entry',
            name='headerline',
            field=models.TextField(default=b'Header Line', max_length=100),
        ),
        migrations.AddField(
            model_name='entry',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'images/%Y/%m/%d'),
        ),
    ]
