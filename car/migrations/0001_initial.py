# Generated by Django 5.1 on 2024-09-10 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_image', models.ImageField(upload_to='uploads/')),
                ('car_description', models.TextField()),
                ('car_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('car_quantity', models.PositiveIntegerField()),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brand.brand')),
            ],
        ),
    ]
