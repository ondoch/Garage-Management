import uuid
from django.db import models
from appointment.models import Appointments

# Create your models here.
class Customer(models.Model):
    public_id = models.UUIDField(
        unique=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    first_name = models.CharField(
        max_length=255,
        null=False
    )
    last_name = models.CharField(
        max_length=255,
        null=False
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        null=False
    )
    email_address = models.EmailField(
        "Email address",
        unique=True
    )
    appointment = models.OneToOneField(
        Appointments,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="customer"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
