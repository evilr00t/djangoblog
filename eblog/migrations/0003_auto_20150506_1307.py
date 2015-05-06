# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eblog', '0002_auto_20150506_0804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='entry',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'static/images/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='eblog.Tag'),
        ),
    ]
