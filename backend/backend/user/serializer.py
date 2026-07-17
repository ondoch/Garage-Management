from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        source = 'public_id',
        read_only = True,
        format = 'hex'
    )
    class Meta:
        model = Customer
        fields = [
            'id',
            'appointment',
            'first_name',
            'last_name',
            'phone_number',
            'email_address',
            'created_at',
            'updated_at',
        ]
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]
