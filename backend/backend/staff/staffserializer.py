from django.db import transaction

from rest_framework import serializers

from authentication.models import User
from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        source="public_id",
        read_only=True,
        format="hex"
    )

    first_name = serializers.CharField(
        source="user.first_name"
    )

    last_name = serializers.CharField(
        source="user.last_name"
    )

    email = serializers.EmailField(
        source="user.email"
    )

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"}
    )

    class Meta:
        model = Staff
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "password",
            "role",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        password = validated_data.pop("password")

        user = User.objects.create_user(
            email=user_data["email"],
            password=password,
            first_name=user_data.get("first_name", ""),
            last_name=user_data.get("last_name", ""),
        )

        staff = Staff.objects.create(
            user=user,
            **validated_data
        )

        return staff

    @transaction.atomic
    def update(self, instance, validated_data):
        user_data = validated_data.pop("user", {})
        password = validated_data.pop("password", None)

        user = instance.user

        user.first_name = user_data.get(
            "first_name",
            user.first_name
        )

        user.last_name = user_data.get(
            "last_name",
            user.last_name
        )

        user.email = user_data.get(
            "email",
            user.email
        )

        if password:
            user.set_password(password)

        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance