# Generated by Django 3.2.23 on 2024-05-21 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magsmenapp', '0016_auto_20240521_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 17, 5, 6, 84963)),
        ),
        migrations.AlterField(
            model_name='media',
            name='CreatedAt',
            field=models.DateField(auto_now_add=True),
        ),
    ]
