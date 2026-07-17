import uuid
from django.db import models
from user.models import Customer

# Create your models here.
class Car(models.Model):
    car_id = models.UUIDField(
        db_index=True,
        editable=False,
        default=uuid.uuid4,
        unique=True
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    make = models.CharField(
        max_length=255,
        null=False
    )
    model = models.CharField(
        max_length=255,
        null=False
    )
    vehicle_reg = models.CharField(
        max_length=15,
        unique=True
    )
    odometer_reading = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.vehicle_reg}"
