# Generated by Django 4.2.13 on 2024-05-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyDineApp', '0005_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='customer_phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='payment',
            name='invoice_number',
            field=models.CharField(max_length=100),
        ),
    ]