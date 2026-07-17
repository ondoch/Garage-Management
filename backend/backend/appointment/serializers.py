from rest_framework import serializers
from .models import Appointments

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email_address',
            'reg_number',
            'reason',
            'status',
        ]
