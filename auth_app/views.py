from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from auth_app.serializer import RegisterSerializer


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serialzer = RegisterSerializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        user = serialzer.save()
        token = Token.objects.create(user=user)
        return Response({'token': str(token.key)})


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        login = request.data.get('login')
        if not User.objects.filter(username=login).exists():
            return Response('Не правильный логин или пароль')
        user = User.objects.get(username=login)
        password = request.data.get('password')
        pass_check = check_password(password, user.password)
        if not pass_check:
            return Response('Не правильный логин ')
        token = Token.objects.get(user=user)
        return Response({'token': str(token.key)})

