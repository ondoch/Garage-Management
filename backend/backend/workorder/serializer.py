from rest_framework import serializers
from .models import WorkOrder

class WorkOrderSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        source = 'public_id',
        read_only = True,
        format='hex'
    )
    class Meta:
        model = WorkOrder
        fields = [
            'id',
            'work_order_number',
            'customer',
            'reg_number',
            'status',
            'created_at',
            'started_at',
            'completed_at',
            'description',
        ]
        read_only_fields = [
            'work_order_number',
            'created_at'
        ]
