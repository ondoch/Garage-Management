from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from authentication.serializers.register import RegisterSerializer

class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            'access':str(refresh.access_token),
            'refresh':str(refresh)
        }
        return Response({
            'user':serializer.data,
            'access':res['access'],
            'refresh':res['refresh']
        }, status=status.HTTP_201_CREATED)
