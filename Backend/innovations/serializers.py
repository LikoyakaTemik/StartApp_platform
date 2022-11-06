from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        validated_data.update({"password": make_password(validated_data.get("password"))})
        return super().create(validated_data)