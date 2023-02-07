from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserRegisterForm
# Create your views here.


def get_all_users(request):
    
    users = User.objects.all()
    
    context = {
        'users': users,   
    }
    
    return render(request, 'profile/all_profiles.html', context)


def get_user_profile(request, username):
    
    user = get_object_or_404(User, username = username)
    
    context = {
        'user': user,   
    }
    
    return render(request, 'profile/single_profile.html', context)


def register_user(request):
    
    if request.method == 'POST':
        register_user_form = UserRegisterForm(request.POST, request.FILES)
        
        
        
        if register_user_form.is_valid():
            
            
            info = register_user_form.cleaned_data
    
            user = User.objects.create_user(
                username= info['username'],
                email= info['email'],
                password= info['password'],
                first_name= info['first_name'],
                last_name= info['last_name'],
            )
            
            # I do this because I've extended the Django's default User to UserProfile to add some extra data 
            user_profile = UserProfile.objects.create(
                user = user,
                image = info['image'],
                bio = info['bio']
            )
            
            user_profile.save()
            
            return redirect('/')
        
    else:
        register_user_form = UserRegisterForm()
        
    return render(request, 'pages/User/register_user.html', {'register_user_form': register_user_form})