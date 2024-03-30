from rest_framework import serializers
from .models import Registration





class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Registration

    