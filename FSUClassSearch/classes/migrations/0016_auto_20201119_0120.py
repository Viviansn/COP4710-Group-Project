# Generated by Django 3.1.2 on 2020-11-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0015_auto_20201119_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='description',
            field=models.TextField(),
        ),
    ]