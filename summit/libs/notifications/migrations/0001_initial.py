# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-30 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CHECKUP', 'Checkup'), ('NONE', 'None')], default='NONE', max_length=10)),
                ('description', models.TextField(help_text='The specific details to the Notification, such as reason, instructions,     etc.')),
                ('seen', models.BooleanField(default=False)),
            ],
        ),
    ]
