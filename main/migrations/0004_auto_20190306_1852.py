# Generated by Django 2.1.5 on 2019-03-06 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190306_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 6, 18, 52, 32, 839139), verbose_name='date puplished:'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_slug',
            field=models.CharField(default=1, max_length=200, unique=True),
        ),
    ]
