# Generated by Django 3.2 on 2022-04-22 15:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_alter_device_warranty_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='warranty_expiry_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 4, 22), null=True),
        ),
    ]
