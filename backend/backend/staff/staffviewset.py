from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Staff
from .staffserializer import StaffSerializer


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]

    queryset = Staff.objects.all()

    lookup_field = "public_id"
    lookup_url_kwarg = "pk"

    http_method_names = [
        "get",
        "post",
        "patch",
    ]