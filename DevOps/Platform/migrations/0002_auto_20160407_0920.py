# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Platform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(blank=True, max_length=50, null=True)),
                ('ip', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]