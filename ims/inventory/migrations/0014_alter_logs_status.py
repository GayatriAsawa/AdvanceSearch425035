# Generated by Django 3.2 on 2022-03-29 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20220329_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='status',
            field=models.CharField(choices=[('Free', 'Free'), ('Allocated', 'Allocated'), ('Decommissioned', 'Decomissioned'), ('Edited', 'Edited'), ('Added', 'Added'), ('Deleted', 'Deleted'), ('Transferred', 'Transferred'), ('Transfer Request Rejected', 'Transfer Request Rejected'), ('Returned To Store', 'Returned To Store')], db_index=True, max_length=100, null=True),
        ),
    ]
