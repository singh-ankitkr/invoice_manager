from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from invoices.models import Invoice, InvoiceItem
from invoices.serializers import InvoiceSerializer, InvoiceItemSerializer


@api_view(['GET', 'POST'])
def invoice_list(request, format=None):
    """
    List all invoices, or create a new invoice.
    """
    if request.method == 'GET':
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def invoice_item(request):
    """
    Create an invoice item
    """
    if request.method == "POST":
        serializer = InvoiceItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def invoice_detail(request, pk):
    """
    Get an invoice with all its items and total cost.
    """
    try:
        invoice = Invoice.objects.get(pk=pk)
        invoice_serializer = InvoiceSerializer(invoice)
        invoice_item_serializer = InvoiceItemSerializer(InvoiceItem.objects.filter(invoice__id=pk), many=True)
        data = invoice_serializer.data
        data["items"] = invoice_item_serializer.data
        data["total"] = sum([ivt["amount"] for ivt in data["items"]])
        return Response(data, status=status.HTTP_200_OK)
    except Invoice.DoesNotExist:
        return Response({"error": f"Invoice id {pk} does not exist"}, status=status.HTTP_404_NOT_FOUND)
