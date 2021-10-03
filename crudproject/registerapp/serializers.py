from .models import RegisterModel
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterModel
        fields = "__all__"