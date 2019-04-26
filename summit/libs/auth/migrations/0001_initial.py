# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-16 22:35
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False, help_text='With this checked, it allows this user to access the administrative backend', verbose_name='Admin site access?')),
                ('external_id', models.CharField(default=uuid.uuid4, max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(blank=True, max_length=300)),
                ('avatar', models.ImageField(blank=True, upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('first_name', models.CharField(default='', max_length=150)),
                ('last_name', models.CharField(default='', max_length=150)),
                ('title', models.CharField(blank=True, max_length=150)),
                ('department', models.CharField(blank=True, max_length=150)),
                ('location', models.CharField(blank=True, max_length=150)),
                ('address', models.TextField(blank=True, max_length=300)),
                ('phone_number', models.CharField(blank=True, max_length=30)),
                ('fax_number', models.CharField(blank=True, max_length=30)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'verbose_name': 'Contact',
                'permissions': (('edit_profile.group', 'Can edit other user profiles of same user group'), ('edit_profile.self', 'Can edit own profile'), ('view_profile.others', 'Can see other user profiles'), ('view_profile.self', 'Can see own profile')),
            },
        ),
        migrations.CreateModel(
            name='CESUnit',
            fields=[
                ('usergroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='summit_auth.UserGroup')),
            ],
            options={
                'verbose_name': 'CES Unit',
            },
            bases=('summit_auth.usergroup',),
        ),
        migrations.CreateModel(
            name='FederalAgency',
            fields=[
                ('usergroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='summit_auth.UserGroup')),
            ],
            options={
                'verbose_name': 'Federal Agency',
            },
            bases=('summit_auth.usergroup',),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('usergroup_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='summit_auth.UserGroup')),
            ],
            options={
                'verbose_name': 'Partner',
            },
            bases=('summit_auth.usergroup',),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='assigned_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='summit_auth.UserGroup'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='auth.Permission', verbose_name='permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='summit_auth.UserGroup'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
