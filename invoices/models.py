from django.db import models


class Invoice(models.Model):
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['date']


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    units = models.IntegerField()
    description = models.CharField(max_length=100)
    amount = models.FloatField()
