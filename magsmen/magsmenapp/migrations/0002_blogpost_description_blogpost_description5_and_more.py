# Generated by Django 4.1.5 on 2023-02-08 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magsmenapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='Description',
            field=models.CharField(default='short description', max_length=2000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Description5',
            field=models.CharField(default='Conclusion description', max_length=2000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Title1',
            field=models.CharField(default='title', max_length=225),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Title14',
            field=models.CharField(default='title', max_length=225),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Title2',
            field=models.CharField(default='title', max_length=225),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='Title3',
            field=models.CharField(default='title', max_length=225),
        ),
    ]