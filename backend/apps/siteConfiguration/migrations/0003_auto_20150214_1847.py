# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteConfiguration', '0002_auto_20150214_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='siteconfiguration',
            old_name='filepath',
            new_name='filespath',
        ),
    ]
