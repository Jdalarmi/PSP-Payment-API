from django.db import models

# Create your models here.

class Transaction(models.Model):
    payment_value = models.FloatField()
    description_transaction = models.CharField(max_length=100)
    method_choices = (
        ('D', 'debit_card'),
        ('C', 'credit_card')
    )
    payment_method = models.CharField(max_length=1, choices=method_choices)
    card_number = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    expiration_date = models.DateField()
    cvv = models.IntegerField()


class Payables(models.Model):
    status_choices = (
        ("P", "paid"),
        ("W", "waiting_founds")
    )
    status = models.CharField(max_length=1, choices=status_choices)
    payment_date = models.DateField()
    avaliable_founds = models.FloatField()
    waiting_founds = models.FloatField()