# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 10:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0006_auto_20151209_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminGroupRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'admin_group_relation',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='admin',
            field=models.ManyToManyField(related_name='managed_groups', through='group.AdminGroupRelation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='admingrouprelation',
            unique_together=set([('user', 'group')]),
        ),
    ]
