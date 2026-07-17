from django.contrib import admin
from .models import Customer
from car.models import Car

# Register your models here.
class CarInLine(admin.TabularInline):
    model = Car
    extra = 0

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [CarInLine]

    list_display = (
        "first_name",
        "last_name",
        "phone_number",
        "email_address",
    )

    search_fields = (
        "first_name",
        "last_name",
        "phone_number",
        "email_address",
    )
