from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    
class AnonymousUser(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

