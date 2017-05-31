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
                ('uname', models.CharField(default=b'', max_length=20)),
                ('upasswd', models.CharField(default=b'', max_length=40)),
                ('ue_mail', models.CharField(default=b'', max_length=30)),
                ('utel', models.IntegerField(null=True)),
                ('rec_name', models.CharField(default=b'', max_length=20)),
                ('rec_tel', models.IntegerField(null=True)),
                ('rec_add', models.CharField(default=b'', max_length=255)),
                ('rec_postcode', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
