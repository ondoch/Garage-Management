from django.contrib import admin
from .models import Appointments

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'phone_number',
        'email_address',
        'reg_number',
        'reason',
        'status',
        'created_at',
    )
    search_fields = (
        'phone_number',
        'email_address',
        'reg_number',
    )

admin.site.register(Appointments, AppointmentAdmin)
