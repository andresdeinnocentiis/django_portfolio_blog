from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, AnonymousUser
from .forms import UserRegisterForm
from django.http import HttpResponse
from rest_framework.response import Response
from django.db import IntegrityError

# Para Autenticar con JWT Token:
from rest_framework_simplejwt.authentication import JWTAuthentication


# Django REST Framework imports:
from .serializers import UserSerializer, UserProfileSerializer, AnonymousUserSerializer, UserSerializerWithToken
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

# Imports para JWT Serializer:
#https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Imports para enviar emails:
from django.core.mail import send_mail
from django.template.loader import render_to_string

# JWT Token Customization:
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        #user_profile_data = UserProfileSerializerWithToken(self.user.userprofile).data
        serializer = UserSerializerWithToken(self.user).data

        #serializer = UserProfileSerializerWithToken(self.user).data
        
        for k, v in serializer.items():
            data[k] = v
        
            
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
# Create your views here.
    

#NOTE: API USER VIEWS:
class GetUserAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the Users.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]
    
class GetSingleUserAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single User.
    '''
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        '''
        Sobrescribimos la función `get_queryset` para poder filtrar el request 
        por medio de la url. En este caso traemos de la url por medio de `self.kwargs` 
        el parámetro `User_id` y con él realizamos una query para traer 
        el User del ID solicitado.  
        '''
        try:
            pk = self.kwargs['pk']
            queryset = User.objects.filter(pk=pk)
            return queryset
        
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        

class RegisterUserAPIView(CreateAPIView):
    __doc__ = f'''
    `[POST]`
    This API view creates a new User.
    '''
    authentication_classes = []
    serializer_class = UserSerializerWithToken
    
    def perform_create(self, serializer):

        password = make_password(serializer.validated_data['password'])
        user = serializer.save(password=password)
        UserProfile.objects.create(user=user)


    
    
class UpdateUserAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a User.
    '''
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

class DestroyUserAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a User.
    '''
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminUser] 
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

#NOTE: API ANONYMOUS USER VIEWS:
class GetAnonymousUserAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the Anonymous Users.
    '''
    queryset = AnonymousUser.objects.all()
    serializer_class = AnonymousUserSerializer
    
    
class GetSingleAnonymousUserAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single Anonymous User.
    '''
    serializer_class = AnonymousUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        '''
        Sobrescribimos la función `get_queryset` para poder filtrar el request 
        por medio de la url. En este caso traemos de la url por medio de `self.kwargs` 
        el parámetro `User_id` y con él realizamos una query para traer 
        el User del ID solicitado.  
        '''
        try:
            anonymous_identifier = self.kwargs['anonymous_identifier']
            queryset = AnonymousUser.objects.filter(anonymous_identifier=anonymous_identifier)
            return queryset
        
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        
class RegisterAnonymousUserAPIView(CreateAPIView):
    __doc__ = f'''
    `[POST]`
    This API view inserts a new Anonymous User on the DataBase.
    '''
    queryset = AnonymousUser.objects.all()
    serializer_class = AnonymousUserSerializer
    
    
class UpdateAnonymousUserAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a Anonymous User.
    '''
    queryset = AnonymousUser.objects.all()
    serializer_class = AnonymousUserSerializer
    

class DestroyAnonymousUserAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes an Anonymous User.
    '''
    queryset = AnonymousUser.objects.all()
    serializer_class = AnonymousUserSerializer