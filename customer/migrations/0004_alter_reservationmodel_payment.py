# Generated by Django 4.2 on 2023-04-19 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_paymentmodel_pdone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.paymenttypemodel'),
        ),
    ]
