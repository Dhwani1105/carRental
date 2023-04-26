# Generated by Django 4.2 on 2023-04-20 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_rename_lice_image_car_car_image'),
        ('customer', '0006_alter_reservationmodel_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.paymenttypemodel'),
        ),
        migrations.AlterField(
            model_name='reservationmodel',
            name='r_car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car'),
        ),
    ]
