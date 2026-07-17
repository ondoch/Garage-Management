import uuid
from django.db import models
from car.models import Car

# Create your models here.
class CarService(models.Model):
    public_id = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    reg_number = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )
    current_mileage = models.PositiveIntegerField()
    next_mileage = models.PositiveIntegerField()
    date = models.DateField(
        auto_now_add=True
    )

    air_cleaner_changed = models.BooleanField(
        default=False
    )
    air_cleaner_checked = models.BooleanField(
        default=False
    )
    battery_water_changed = models.BooleanField(
        default=False
    )
    battery_water_checked = models.BooleanField(
        default=False
    )
    brake_fluid_changed = models.BooleanField(
        default=False
    )
    brake_fluid_checked = models.BooleanField(
        default=False
    )
    brake_pad_changed = models.BooleanField(
        default=False
    )
    brake_pad_checked = models.BooleanField(
        default=False
    )
    brake_lining_changed = models.BooleanField(
        default=False
    )
    brake_lining_checked = models.BooleanField(
        default=False
    )
    cooling_system_changed = models.BooleanField(
        default=False
    )
    cooling_system_checked = models.BooleanField(
        default=False
    )
    engine_oil_changed = models.BooleanField(
        default=False
    )
    engine_oil_checked = models.BooleanField(
        default=False
    )
    fuel_filter_changed = models.BooleanField(
        default=False
    )
    fuel_filter_checked = models.BooleanField(
        default=False
    )
    gearbox_changed = models.BooleanField(
        default=False
    )
    gearbox_checked = models.BooleanField(
        default=False
    )
    oil_filter_changed = models.BooleanField(
        default=False
    )
    oil_filter_checked = models.BooleanField(
        default=False
    )
    steering_fluid_changed = models.BooleanField(
        default=False
    )
    steering_fluid_checled = models.BooleanField(
        default=False
    )
    spark_plug_changed = models.BooleanField(
        default=False
    )
    spark_plug_checked = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.reg_number}"
