from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer as BaseUserSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomUserSerializer(BaseUserSerializer):
    dateOfregistration = serializers.DateTimeField(source='date_joined', read_only=True)
    class Meta(BaseUserSerializer.Meta):

        model = User
        
        fields = ('id', 'uuid', 'username', 'email', 'role', 'balance', 'avatar', 'description', 'dateOfregistration')
class AllPublicUsersSerializer(BaseUserSerializer):
    dateOfregistration = serializers.DateTimeField(source='date_joined', read_only=True)
    class Meta(BaseUserSerializer.Meta):

        model = User
        
        fields = ('uuid', 'username', 'avatar', 'description', 'dateOfregistration')


class CustomUserCreateSerializer(BaseUserRegistrationSerializer):
    dateOfregistration = serializers.DateTimeField(source='date_joined', read_only=True)
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = User
        fields = ('id', 'uuid', 'username', 'email', 'password', 'role', 'dateOfregistration')


class PublicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'username', 'description', 'avatar')

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('uuid', 'username', 'description', 'avatar')
    