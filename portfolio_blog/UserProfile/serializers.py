from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import UserProfile, AnonymousUser
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings



class UserProfileSerializer(serializers.ModelSerializer):
    #user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['linkedin', 'bio', 'image']
    
    
class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    bio = serializers.SerializerMethodField()
    linkedin = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    #userprofile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ['id', 'username','password', 'email', 'first_name', 'last_name', 'isAdmin', 'token', 'linkedin', 'bio', 'image']


    def get_isAdmin(self, obj):
        return obj.is_staff
    
    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
    

    def get_bio(self, obj):
        return obj.userprofile.bio
    
    def get_linkedin(self, obj):
        return obj.userprofile.linkedin
    
    def get_image(self, obj):
        if obj.userprofile.image:
            return f"{settings.MEDIA_URL}{obj.userprofile.image}"
        return None

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
   

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'email', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)

class AnonymousUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousUser
        fields = '__all__'