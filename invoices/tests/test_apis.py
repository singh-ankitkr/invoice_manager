from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from ..models import Invoice, InvoiceItem
from ..serializers import InvoiceSerializer, InvoiceItemSerializer

client = Client()


class GetAllInvoicesTest(TestCase):
    """ Test module for GET all invoices api"""

    def setUp(self):
        Invoice.objects.create(date="2022-01-01", customer_name="Test customer 1")
        Invoice.objects.create(date="2022-02-02", customer_name="Test customer 2")
        Invoice.objects.create(date="2022-03-03", customer_name="Test customer 3")

    def test_get_all_invoices(self):
        # get API response
        response = client.get(reverse('get_post_invoices'))
        # get data from db
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetInvoiceFullTest(TestCase):
    """ Test module to get the full invoice along with the invoice items """

    def setUp(self):
        self.invoice = Invoice.objects.create(date="2022-02-01", customer_name="Test customer 1")
        InvoiceItem.objects.create(invoice=self.invoice, units=4, description="Test goods 1", amount=400)
        InvoiceItem.objects.create(invoice=self.invoice, units=5, description="Test goods 2", amount=500)
        InvoiceItem.objects.create(invoice=self.invoice, units=6, description="Test goods 3", amount=600)

    def test_get_full_invoice(self):
        # get API response
        response = client.get(reverse('get_full_invoice', kwargs={'pk': self.invoice.id}))
        # get data from db
        inv = Invoice.objects.get(pk=self.invoice.id)
        serializer_invoice = InvoiceSerializer(inv)
        inv_items = InvoiceItem.objects.filter(invoice__id=self.invoice.id)
        serializer_invoice_items = InvoiceItemSerializer(inv_items, many=True)
        inv_data = serializer_invoice.data
        inv_data["items"] = serializer_invoice_items.data
        inv_data["total"] = 1500
        self.assertEqual(response.data, inv_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
