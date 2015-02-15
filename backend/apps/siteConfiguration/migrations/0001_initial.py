# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteConfiguration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filepath', models.CharField(default=b'files', max_length=255, verbose_name=b'Path for downloaded/uploaded files')),
            ],
            options={
                'verbose_name': 'Site configuration',
            },
            bases=(models.Model,),
        ),
    ]
