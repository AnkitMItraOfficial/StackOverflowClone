# Generated by Django 3.1 on 2020-10-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0005_auto_20201024_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
