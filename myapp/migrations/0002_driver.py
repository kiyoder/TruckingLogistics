# Generated by Django 5.1.1 on 2024-11-20 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('driver_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.booking')),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.container')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
            ],
        ),
    ]
