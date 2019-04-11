# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-11 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('summit_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('html_body', models.TextField(default='')),
                ('is_published', models.BooleanField(default=False)),
                ('groups', models.CharField(choices=[(1, 'Public'), (1, 'Partner'), (2, 'CESUnit'), (3, 'FederalAgency')], default=0, max_length=100)),
                ('authors', models.ManyToManyField(to='summit_auth.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('page_id', models.CharField(max_length=255)),
                ('documents', models.ManyToManyField(to='summit_docs.Document')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
