import uuid

from django.db import models
from django.conf import settings


class Role(models.TextChoices):
    ADMIN = "ADMIN", "Administrator"
    STAFF = "STAFF", "Staff"


class Staff(models.Model):

    public_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="staff_profile"
    )

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STAFF
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    @property
    def first_name(self):
        return self.user.first_name
    
    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email
    