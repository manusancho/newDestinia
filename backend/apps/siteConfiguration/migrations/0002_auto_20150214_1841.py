# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteConfiguration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='filepath',
            field=models.CharField(default=b'files', help_text=b'Path for downloaded/uploaded files', max_length=255, verbose_name=b'Files path'),
            preserve_default=True,
        ),
    ]
