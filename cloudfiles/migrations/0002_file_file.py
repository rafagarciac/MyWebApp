# Generated by Django 2.1.1 on 2018-10-13 19:24

import cloudfiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudfiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default=None, upload_to=cloudfiles.models.filesPath),
        ),
    ]
