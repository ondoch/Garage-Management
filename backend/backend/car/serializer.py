from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        source='car_id',
        default='hex',
        read_only=True
    )
    class Meta:
        model = Car
        fields = [
            'id',
            'customer',
            'make',
            'model',
            'vehicle_reg',
            'odometer_reading',
        ]
        read_only_fields = (
            "id",
        )
