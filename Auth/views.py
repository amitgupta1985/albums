from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.views import APIView
from .serializers import LoginSerializer,RegisterUserSerializer
from django.contrib.auth import login as userlogin, logout as userlogout
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

class LoginAPIView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        userlogin(request, user)
        token,created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key},status=status.HTTP_200_OK)

class LogoutAPIView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        userlogout(request)
        return Response(status=status.HTTP_204_NO_CONTENT) 

class RegisterAPIView(APIView):

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)               







