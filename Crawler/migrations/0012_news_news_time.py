# Generated by Django 3.0.7 on 2020-07-27 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crawler', '0011_auto_20200727_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_time',
            field=models.CharField(default='', max_length=200, verbose_name='News Time'),
            preserve_default=False,
        ),
    ]
