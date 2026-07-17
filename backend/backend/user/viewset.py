from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializer import CustomerSerializer
from .models import Customer

class CustomerViewset(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    http_method_names = ['post', 'get']
    permission_classes = (AllowAny,)
    queryset = Customer.objects.all()
