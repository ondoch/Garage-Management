from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Quotation
from .serializer import QuotationSerializer


class QuotationViewSet(viewsets.ModelViewSet):
    serializer_class = QuotationSerializer
    permission_classes = (AllowAny,)
    lookup_field = "public_id"

    def get_queryset(self):
        return (
            Quotation.objects
            .select_related(
                "customer",
                "vehicle_reg",
                "work_order_number",
            )
            .prefetch_related("items")
            .order_by("-date")
        )