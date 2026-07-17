from django.contrib import admin
from .models import Invoice

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'work_order',
        'payment_status',
        'method_of_payment',
    )
    search_fields = (
        'work_order',
    )

admin.site.register(Invoice, InvoiceAdmin)
