# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('upasswd', models.CharField(max_length=40)),
                ('ue_mail', models.CharField(max_length=30)),
                ('utel', models.CharField(max_length=11)),
                ('rec_name', models.CharField(default=b'', max_length=20)),
                ('rec_tel', models.CharField(default=b'', max_length=11)),
                ('rec_add', models.CharField(default=b'', max_length=255)),
                ('rec_postcode', models.CharField(default=b'', max_length=6)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
