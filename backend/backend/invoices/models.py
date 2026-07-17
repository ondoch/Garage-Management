import uuid
from django.db import models
from workorder.models import WorkOrder
from quotation.models import Quotation

# Create your models here.
class PaymentStatus(models.TextChoices):
    UNPAID = 'UNPAID', 'Unpaid'
    PAID = 'PAID', 'Paid'
    PARTIAL_PAYMENT = 'PARTIAL_PAID', 'Partial paid'

class PaymentMethod(models.TextChoices):
    CASH = 'CASH', 'Cash'
    MPESA = 'MPESA', 'Mpesa'
    BANK = 'BANK', 'Bank'

class Invoice(models.Model):
    public_id = models.UUIDField(
        db_index=True,
        unique=True,
        editable=False,
        default=uuid.uuid4
    )
    work_order = models.ForeignKey(
        WorkOrder,
        on_delete=models.CASCADE
    )
    quotation_number = models.ForeignKey(
        Quotation,
        on_delete=models.CASCADE
    )
    payment_status = models.CharField(
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNPAID
    )
    method_of_payment = models.CharField(
        choices=PaymentMethod.choices,
        default=PaymentMethod.CASH
    )
