# Generated by Django 5.0.6 on 2024-07-03 11:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magsmenapp', '0037_alter_careerinfo_expertiseno_alter_contactdata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 3, 16, 34, 14, 655560)),
        ),
    ]
