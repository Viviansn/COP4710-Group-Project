# Generated by Django 3.1.2 on 2020-11-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_auto_20201118_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
