from rest_framework import serializers

from .models import Quotation, QuotationItem


class QuotationItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = QuotationItem
        fields = [
            "id",
            "product",
            "quantity",
            "unit_price",
            "total_price",
        ]


class QuotationSerializer(serializers.ModelSerializer):
    items = QuotationItemSerializer(many=True)

    total_amount = serializers.ReadOnlyField()

    class Meta:
        model = Quotation
        fields = [
            "id",
            "public_id",
            "quotation_number",
            "work_order_number",
            "customer",
            "vehicle_reg",
            "date",
            "items",
            "total_amount",
        ]

        read_only_fields = [
            "id",
            "public_id",
            "quotation_number",
            "date",
            "total_amount",
        ]

    def create(self, validated_data):
        items_data = validated_data.pop("items")

        quotation = Quotation.objects.create(
            **validated_data
        )

        QuotationItem.objects.bulk_create([
            QuotationItem(
                quotation=quotation,
                **item_data
            )
            for item_data in items_data
        ])

        return quotation