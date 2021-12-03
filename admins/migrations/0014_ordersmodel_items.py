# Generated by Django 3.2.9 on 2021-12-03 13:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0013_ordersmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersmodel',
            name='items',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None),
        ),
    ]