# Generated by Django 5.1.1 on 2024-12-11 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='delivered_at',
        ),
        migrations.RemoveField(
            model_name='container',
            name='received_by',
        ),
        migrations.RemoveField(
            model_name='containerstatus',
            name='received_by',
        ),
        migrations.RemoveField(
            model_name='containerstatus',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(default='Ongoing', max_length=255),
        ),
    ]
