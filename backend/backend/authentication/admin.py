from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User
from .forms import UserCreationForm, UserChangeForm

from staff.models import Staff

class StaffInline(admin.StackedInline):
    model = Staff
    can_delete = False
    extra = 0

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User

    inlines = [StaffInline]

    list_display = (
        "email",
        "is_staff",
        "is_superuser",
        "is_active",
    )

    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
    )

    ordering = ("email",)

    search_fields = ("email",)

    fieldsets = (
        (None, {
            "fields": ("email", "password")
        }),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important Dates", {
            "fields": ("last_login", "date_joined")
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
            ),
        }),
    )

admin.site.register(User, UserAdmin)
