from django.contrib import admin
from .models import WorkOrder

# Register your models here.
class WorkOrderAdmin(admin.ModelAdmin):
    list_display = (
        'work_order_number',
        'customer',
        'reg_number',
        'status',
        'created_at',
        'started_at',
        'completed_at',
    )
    search_fields = (
        'customer',
    )

admin.site.register(WorkOrder, WorkOrderAdmin)
