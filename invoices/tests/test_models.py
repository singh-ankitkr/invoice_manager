from django.test import TestCase
from ..models import Invoice, InvoiceItem
from datetime import datetime


class InvoiceTest(TestCase):
    """ Test module for Invoice model """

    def setUp(self):
        Invoice.objects.create(date="2022-02-03", customer_name="Test customer")

    def test_invoice(self):
        invoices = Invoice.objects.all()
        self.assertEqual(len(invoices), 1)
        invoice = invoices[0]
        invoice_date = datetime.date(datetime.fromisoformat("2022-02-03"))
        self.assertEqual(invoice.customer_name, "Test customer")
        self.assertEqual(invoice.date, invoice_date)


class InvoiceItemTest(TestCase):
    """ Test module for InvoiceItem model """

    def setUp(self):
        invoice = Invoice.objects.create(date="2022-02-03", customer_name="Test customer")
        InvoiceItem.objects.create(invoice=invoice, units=5, description="Test goods", amount=400)

    def test_invoice_item(self):
        invoice = Invoice.objects.get(customer_name="Test customer")
        invoice_item = InvoiceItem.objects.all()
        self.assertEqual(len(invoice_item), 1)
        invoice_item = invoice_item[0]
        self.assertEqual(invoice_item.invoice, invoice)
        self.assertEqual(invoice_item.units, 5)
        self.assertEqual(invoice_item.description, "Test goods")
        self.assertEqual(invoice_item.amount, 400)
