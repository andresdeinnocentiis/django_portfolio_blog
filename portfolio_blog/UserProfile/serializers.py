from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import UserProfile, AnonymousUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    id = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']
        
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = UserProfile
        fields = ['user', 'image', 'bio']
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        
        user = User.objects.create_user(**user_data)
        user_profile = UserProfile.objects.create(user=user, **validated_data)

        return user_profile

class AnonymousUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonymousUser
        fields = '__all__'