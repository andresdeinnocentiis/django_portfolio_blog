from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    linkedin = models.TextField(null=True, blank=True, default="")
    image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    
class AnonymousUser(models.Model):
    username = models.CharField(max_length=100, blank=True)
    anonymous_identifier = models.CharField(max_length=255, unique=True)
    
    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        self.username = self.username.replace(" ", "_")
        return super(AnonymousUser, self).save(*args, **kwargs)
    
    def __str__(self):
        if self.username:
            return self.username
        else:
            return self.anonymous_identifier

