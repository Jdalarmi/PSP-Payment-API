# Generated by Django 4.2.6 on 2023-10-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_transaction_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='card_number',
            field=models.CharField(default='1232-2222-2222-2222', max_length=18),
        ),
    ]
