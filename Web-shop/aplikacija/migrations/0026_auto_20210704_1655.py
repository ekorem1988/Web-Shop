# Generated by Django 3.1.12 on 2021-07-04 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacija', '0025_auto_20210704_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartpay',
            name='cijena',
        ),
        migrations.RemoveField(
            model_name='cartpay',
            name='cijena2',
        ),
        migrations.AddField(
            model_name='cartpay',
            name='email',
            field=models.EmailField(default=1, max_length=60, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 16, 54, 48, 128907)),
        ),
    ]
