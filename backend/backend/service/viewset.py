from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializer import ServiceSerializer
from .models import CarService

class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    http_method_names = ['post', 'get']
    lookup_field = 'public_id'
    permission_classes = (AllowAny,)
    queryset = CarService.objects.all()
