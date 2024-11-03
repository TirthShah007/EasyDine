# Generated by Django 4.2.13 on 2024-05-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyDineApp', '0007_delete_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('people', models.IntegerField()),
                ('invoice_number', models.CharField(max_length=20)),
                ('total_payment', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
