from rest_framework import serializers
from hello.models import login

class loginSerializers(serializers.ModelSerializer):
    class Meta:
        model=login
        fields='__all__'
