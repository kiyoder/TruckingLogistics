# Generated by Django 5.1.1 on 2024-11-21 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='license_number',
            field=models.CharField(default='UNKNOWN', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to='myapp.booking'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='container',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to='myapp.container'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers', to='myapp.customer'),
        ),
    ]
