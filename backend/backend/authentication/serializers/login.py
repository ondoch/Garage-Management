from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from staff.staffserializer import StaffSerializer
from staff.models import Staff

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        try:
            staff = self.user.staff_profile
            data["user"] = StaffSerializer(staff).data
        except Staff.DoesNotExist:
            data["user"] = None

        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        return data
