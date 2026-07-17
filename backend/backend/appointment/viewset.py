from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import AppointmentSerializer
from .models import Appointments

class AppointmentViewset(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    serializer_class = AppointmentSerializer
    lookup_field = 'phone_number'
    queryset = Appointments.objects.all()
