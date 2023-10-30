import re
from django.db import models
from django.utils import timezone
# Create your models here.

class Transaction(models.Model):
    payment_value = models.FloatField()
    description_transaction = models.CharField(max_length=100)
    method_choices = (
        ('D', 'debit_card'),
        ('C', 'credit_card')
    )
    payment_method = models.CharField(max_length=1, choices=method_choices)
    card_number = models.CharField(max_length=18, default='1232-2222-2222-2222')
    customer_name = models.CharField(max_length=50)
    expiration_date = models.DateField()
    cvv = models.IntegerField()

    def value_return(value, method):
        if method == 'D':
            value_debit = value-(value * 0.03)
            Payables.objects.create(status= 'P', payment_date=timezone.now(),avaliable_founds=value_debit)
        else:
            value_credit = value-(value * 0.05)
            Payables.objects.create(status= 'W', payment_date=timezone.now() + timezone.timedelta(days=30),waiting_founds=value_credit)

    def mask(self):
        return "*" * 15 + self.card_number[-4:]


class Payables(models.Model):
    status_choices = (
        ("P", "paid"),
        ("W", "waiting_founds")
    )
    status = models.CharField(max_length=1, choices=status_choices)
    payment_date = models.DateField()
    avaliable_founds = models.FloatField(blank=True, null=True)
    waiting_founds = models.FloatField(blank=True, null=True)