from rest_framework import serializers
from .models import CarService

class ServiceSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        source = 'public_id',
        format = 'hex',
        read_only = True
    )

    class Meta:
        model = CarService
        fields = [
            'id',
            'reg_number',
            'current_mileage',
            'next_mileage',
            'date',
            'air_cleaner_changed',
            'air_cleaner_checked',
            'battery_water_changed',
            'battery_water_checked',
            'brake_fluid_changed',
            'brake_fluid_checked',
            'brake_pad_changed',
            'brake_pad_checked',
            'brake_lining_changed',
            'brake_lining_checked',
            'cooling_system_changed',
            'cooling_system_checked',
            'engine_oil_changed',
            'engine_oil_checked',
            'fuel_filter_changed',
            'fuel_filter_checked',
            'gearbox_changed',
            'gearbox_checked',
            'oil_filter_changed',
            'oil_filter_checked',
            'steering_fluid_changed',
            'steering_fluid_checled',
            'spark_plug_changed',
            'spark_plug_checked',
        ]
