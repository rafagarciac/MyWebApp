# Generated by Django 2.1a1 on 2018-07-11 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_textcontent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Rafael García', max_length=50),
        ),
        migrations.AddField(
            model_name='post',
            name='section',
            field=models.CharField(default='General', max_length=50),
        ),
    ]
