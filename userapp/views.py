from django.shortcuts import render

# Create your views here.

# from rest_framework.routers import JSONRenderer

from rest_framework.viewsets import ModelViewSet
from .serializers import UserModelSerializer
from .models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
