# Generated by Django 4.1.5 on 2023-02-08 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magsmenapp', '0005_alter_blogpost_description1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='Description1',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='Description2',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='Description3',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='Description4',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
