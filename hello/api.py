from hello.models import login
from rest_framework import viewsets, permissions
from .serializers import loginSerializers

class LoginViewSet(viewsets.ModelViewSet):
    queryset=login.objects.all()
    permission_classes=[
        permissions.AllowAny 
    ]
    serializer_class= loginSerializers