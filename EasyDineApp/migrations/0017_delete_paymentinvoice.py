# Generated by Django 4.2.13 on 2024-05-17 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EasyDineApp', '0016_rename_customer_name_paymentinvoice_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentInvoice',
        ),
    ]