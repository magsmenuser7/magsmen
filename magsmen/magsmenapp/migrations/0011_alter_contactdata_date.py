# Generated by Django 4.1 on 2024-05-15 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magsmenapp', '0010_contactdata_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 15, 23, 28, 13, 441023)),
        ),
    ]
