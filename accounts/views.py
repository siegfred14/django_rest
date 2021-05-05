# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.


class UserCreate(APIView):
    def post(self, request, format='json'):
        return Response("hello")
