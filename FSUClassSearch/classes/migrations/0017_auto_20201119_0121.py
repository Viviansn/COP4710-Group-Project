# Generated by Django 3.1.2 on 2020-11-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0016_auto_20201119_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
