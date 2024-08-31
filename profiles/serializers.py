from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from profiles.models import User
from rest_framework import serializers

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ('id', 'name', 'email', 'bio', 'is_active', 'created_at', 'updated_at')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'bio', 'is_active', 'created_at', 'updated_at')

        

    