import uuid
import random
import string
from django.db import models
from user.models import Customer
from car.models import Car

def generate_work_order():
    return "WO-" + "".join(
        random.choices(string.ascii_uppercase + string.digits, k=8)
    )

# Create your models here.
class Status(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    IN_PROGRESS = 'IN_PROGRESS', 'In progress'
    AWAITING_PARTS = 'AWAITING_PARTS', 'Awaiting parts'
    COMPLETED = 'COMPLETED', 'Completed'
    CANCELLED = 'CANCELLED', 'Cancelled'

class WorkOrder(models.Model):
    public_id = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        unique=True,
        editable=False
    )
    work_order_number = models.CharField(
        max_length=20,
        unique=True,
        default=generate_work_order,
        editable=False
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='customer'
    )
    reg_number = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='car'
    )
    status = models.CharField(
        choices = Status.choices,
        default = Status.IN_PROGRESS
    )
    created_at = models.DateField(
        auto_now_add=True
    )
    started_at = models.DateField()
    completed_at = models.DateField(
        null=True,
        blank=True
    )
    description = models.TextField(
        null=False
    )

    def __str__(self):
        return f"{self.work_order_number}"
