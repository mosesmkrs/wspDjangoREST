# Generated by Django 5.2 on 2025-05-02 09:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=10)),
                ('capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=20, unique=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_phone', models.CharField(max_length=20)),
                ('hotel_name', models.CharField(default='Blue Lagoon Hotels and Resorts', max_length=100)),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('number_of_rooms', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('extra_bed', models.BooleanField(default=False)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('reservation_time', models.DateTimeField(auto_now_add=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservations.roomtype')),
            ],
        ),
    ]
