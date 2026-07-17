from rest_framework import serializers
from staff.models import Staff
from staff.staffserializer import StaffSerializer

class RegisterSerializer(StaffSerializer):
    password = serializers.CharField(
        max_length = 128,
        write_only = True,
        required = True
    )
    class Meta:
        model = Staff
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "role",
        ]
    def create(self, validated_data):
        return super().create(validated_data)
