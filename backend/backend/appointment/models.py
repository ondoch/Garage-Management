import uuid
from django.db import models

# Create your models here.
class Status(models.TextChoices):
    SCHEDULED = 'SCHEDULED', 'Scheduled'
    CONFIRMED = 'CONFIRMED', 'Confirmed'
    CANCELLED = 'CANCELLED', 'Cancelled'

class Appointments(models.Model):
    public_id = models.UUIDField(
        db_index=True,
        editable=False,
        default=uuid.uuid4,
        unique=True
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
    reg_number = models.CharField(
        max_length=15,
        null=False 
    )
    reason = models.TextField(
        null=False
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SCHEDULED
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.reg_number}"
