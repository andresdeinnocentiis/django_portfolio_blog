from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile
# Create your views here.


def get_all_profiles(request):
    
    users = User.objects.all()
    #profile = UserProfile.objects.get(user = user)
    
    context = {
        'users': users,   
    }
    
    return render(request, 'profile/all_profiles.html', context)

def get_user_profile(request, username):
    
    user = get_object_or_404(User, username = username)
    #profile = UserProfile.objects.get(user = user)
    
    context = {
        'user': user,   
    }
    
    return render(request, 'profile/single_profile.html', context)