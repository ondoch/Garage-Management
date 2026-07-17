from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializer import CarSerializer
from .models import Car

class CarViewset(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    http_method_names = ['post', 'get']
    permission_classes = (AllowAny,)
    queryset = Car.objects.all()
