# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-16 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wafer.snippets.markdown_field


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_scheduleitem_expand'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleitem',
            name='last_updated',
            field=models.DateTimeField(auto_now=True, help_text='Date & Time this was last updated', null=True),
        ),
    ]
