from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializer import InvoiceSerializer
from .models import Invoice

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    http_method_names = ['post', 'get']
    permission_classes = (AllowAny,)
    queryset = Invoice.objects.all()
