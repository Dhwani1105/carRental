# Generated by Django 4.2 on 2023-04-20 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_reservationmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('DELIVERED', 'DELIVERED'), ('CANCEL', 'CANCEL'), ('RETURN', 'RETURN')], max_length=100, null=True),
        ),
    ]
