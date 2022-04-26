# Generated by Django 3.2 on 2022-02-20 08:58

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0007_alter_device_warranty_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='allocation_status',
            field=models.CharField(choices=[('IQC', 'IQC'), ('Allocated', 'Allocated'), ('Decommissioned', 'Decommissioned'), ('Free', 'Free'), ('Needs Maintainence', 'Needs Maintainence')], default='IQC', max_length=20),
        ),
        migrations.AlterField(
            model_name='device',
            name='employee',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='device',
            name='floor_number',
            field=models.CharField(blank=True, choices=[('1F', '1'), ('2F', '2'), ('3F', '3'), ('4F', '4')], default='1F', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='gin_initials',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gin_initials', to='inventory.poini'),
        ),
        migrations.AlterField(
            model_name='device',
            name='gin_year',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gin_year', to='inventory.poyear'),
        ),
        migrations.AlterField(
            model_name='device',
            name='loc_number',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='device',
            name='loc_type',
            field=models.CharField(blank=True, choices=[('D', 'Desk'), ('S', 'Cupboard'), ('Q', 'Incomming Quality Control'), ('E', 'External')], default='Q', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='project',
            field=models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.projectmaster'),
        ),
        migrations.AlterField(
            model_name='device',
            name='warranty_expiry_date',
            field=models.DateField(blank=True, default=datetime.date(2022, 2, 20), null=True),
        ),
        migrations.AlterField(
            model_name='projectmaster',
            name='name',
            field=models.CharField(default='Not Assigned to Any Project', max_length=255),
        ),
        migrations.AlterField(
            model_name='projectmaster',
            name='project_id',
            field=models.PositiveIntegerField(default=0, unique=True, validators=[django.core.validators.MaxValueValidator(99999999), django.core.validators.MinValueValidator(0)]),
        ),
    ]