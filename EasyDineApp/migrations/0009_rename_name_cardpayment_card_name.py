# Generated by Django 4.2.13 on 2024-05-16 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EasyDineApp', '0008_cardpayment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardpayment',
            old_name='name',
            new_name='card_name',
        ),
    ]