# Generated by Django 3.1.12 on 2021-06-22 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacija', '0009_auto_20210622_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 23, 15, 35, 28, 988721)),
        ),
    ]
