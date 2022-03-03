from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from invoices import views


urlpatterns = [
    path('invoices/', views.invoice_list, name="get_post_invoices"),
    path('invoiceitem/', views.invoice_item, name="post_invoices"),
    path('invoices/<int:pk>/', views.invoice_detail, name="get_full_invoice"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
