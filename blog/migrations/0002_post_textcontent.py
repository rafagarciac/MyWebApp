# Generated by Django 2.1a1 on 2018-07-08 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='textcontent',
            field=models.TextField(default='Some text'),
        ),
    ]
