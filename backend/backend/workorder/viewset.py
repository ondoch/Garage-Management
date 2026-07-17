from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializer import WorkOrderSerializer
from .models import WorkOrder

class WorkOrderViewSet(viewsets.ModelViewSet):
    serializer_class = WorkOrderSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post', 'get']
    queryset = WorkOrder.objects.all()
