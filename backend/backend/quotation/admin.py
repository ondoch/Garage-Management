from django.contrib import admin
from .models import Quotation, QuotationItem


class QuotationItemInline(admin.TabularInline):
    model = QuotationItem
    extra = 1

    # Display the line total for each item
    readonly_fields = ("total_price",)

    def total_price(self, obj):
        if obj.pk:
            return obj.total_price
        return 0

    total_price.short_description = "Total Price"


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = (
        "quotation_number",
        "work_order_number",
        "vehicle_reg",
        "customer",
        "date",
        "total_amount",
    )

    search_fields = (
        "quotation_number",
    )

    readonly_fields = (
        "quotation_number",
        "date",
        "total_amount",
    )

    inlines = [
        QuotationItemInline,
    ]

    def total_amount(self, obj):
        return obj.total_amount

    total_amount.short_description = "Quotation Total"
    