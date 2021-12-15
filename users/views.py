from django.contrib.auth import get_user_model
from django.shortcuts import render
from djoser import views
from ping3 import ping
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Ping
from .serializers import PingSerializer

CustomUser = get_user_model()


class CustomUserViewSet(views.UserViewSet):

    lookup_field = 'id'


class PingGoogle(GenericAPIView):
    def get(self, request):

        latency = ping('google.com')*1000
        data = Ping(latency=round(latency, 2))
        serializer = PingSerializer(data)
        return Response(serializer.data)

