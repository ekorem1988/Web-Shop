# Generated by Django 3.1.12 on 2021-07-10 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacija', '0042_auto_20210710_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_start_pay',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 11, 17, 59, 3, 188645)),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 11, 17, 59, 3, 187635)),
        ),
    ]