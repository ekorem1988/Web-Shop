# Generated by Django 3.1.12 on 2021-07-06 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacija', '0034_auto_20210705_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=60),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 7, 21, 20, 47, 468824)),
        ),
    ]