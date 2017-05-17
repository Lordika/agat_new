# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 10:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('file', models.FilePathField(path='D:\\agat_new\\agat_web\\agatweb\\static')),
                ('taskId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.Task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
