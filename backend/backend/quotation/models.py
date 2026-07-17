import string
import random
import uuid
from decimal import Decimal

from django.db import models

from car.models import Car
from user.models import Customer
from workorder.models import WorkOrder


def generate_quotation_no():
    return "QA-" + "".join(
        random.choices(string.ascii_uppercase + string.digits, k=8)
    )


class Quotation(models.Model):
    public_id = models.UUIDField(
        db_index=True,
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    quotation_number = models.CharField(
        max_length=20,
        unique=True,
        default=generate_quotation_no,
        editable=False
    )

    work_order_number = models.ForeignKey(
        WorkOrder,
        on_delete=models.CASCADE
    )

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="quotations"
    )

    vehicle_reg = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name="quotations"
    )

    date = models.DateField(
        auto_now_add=True
    )

    @property
    def total_amount(self):
        return sum(
            (item.total_price for item in self.items.all()),
            Decimal("0.00")
        )

    def __str__(self):
        return self.quotation_number


class QuotationItem(models.Model):
    quotation = models.ForeignKey(
        Quotation,
        related_name="items",
        on_delete=models.CASCADE
    )

    product = models.CharField(
        max_length=255
    )

    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    @property
    def total_price(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.product}"