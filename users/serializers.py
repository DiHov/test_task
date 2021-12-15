from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db import transaction
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from .models import CustomUser

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    id_type = serializers.SerializerMethodField()

    def get_id_type(self, user):
        if '@' in user.id:
            return 'mail'
        if user.id.isdigit() and len(user.id) == 10:
            return 'phone'

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'id_type',
        )


class CustomUserCreateSerializer(UserCreateSerializer):
    id = serializers.CharField()
    # id_type = serializers.SerializerMethodField()

    def validate_id(self, value):
        return value

    def validate_password(self, value):
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    def get_id_type(self, user):
        print(user)
        # print(self.data['id'])
        if '@' in user.id:
            return 'mail'
        if user.id.isdigit() and len(user.id) == 10:
            return 'phone'

    class Meta:
        model = User
        fields = (
            'id',
            'password',
        )

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create(**validated_data)
        return user


class PingSerializer(serializers.Serializer):
    latency = serializers.FloatField()
