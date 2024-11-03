# Generated by Django 4.2.13 on 2024-05-16 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyDineApp', '0011_delete_cardpayment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=100)),
                ('booking_datetime', models.DateTimeField()),
                ('booking_name', models.CharField(max_length=100)),
                ('total_people', models.IntegerField()),
                ('total_payment', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]