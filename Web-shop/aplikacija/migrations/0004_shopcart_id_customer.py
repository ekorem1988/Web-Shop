# Generated by Django 3.1.12 on 2021-06-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacija', '0003_auto_20210612_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='id_customer',
            field=models.CharField(max_length=100, null=True),
        ),
    ]