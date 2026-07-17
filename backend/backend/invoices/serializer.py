from rest_framework import serializers
from .models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        source = 'public_id',
        read_only = True,
        format = 'hex'
    )

    class Meta:
        model = Invoice
        fields = [
            'id',
            'work_order',
            'quotation_number',
            'payment_status',
            'method_of_payment',
        ]
