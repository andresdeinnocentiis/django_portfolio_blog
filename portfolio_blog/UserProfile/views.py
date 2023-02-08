from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from .forms import UserRegisterForm
from django.http import HttpResponse
# Create your views here.


def get_all_users(request):
    
    users = User.objects.all()
    
    context = {
        'users': users,   
    }
    
    return render(request, 'pages/User/all_users.html', context)


def get_user(request, id):
    
    if id:
        user = get_object_or_404(User, id = id)
    else:
        id = request.GET['id']
        user = get_object_or_404(User, id = id)
    context = {
        'user': user,   
    }
    
    return render(request, 'pages/User/single_user.html', context)


def login_user(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
            
    else:
        form = AuthenticationForm()
    return render(request, 'pages/User/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return(redirect('home'))


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



def search_user(request):
    
    return render(request, 'pages/User/search_user.html')


def search_user_result(request):
    
    if request.GET['username']:
        
        username = request.GET['username']
        
        # Se que se podría haber usado simplemente User.objects.get(username = username)) xq es un dato que no se repite, pero quería probar un metodo distinto
        user = User.objects.get(username = username)
        user_profile = UserProfile.objects.get(user=user)
        
        return render(request, 'pages/User/search_user_result.html', {"user": user_profile, "username": username})
    
    else:
        
        response = "You haven't sent any data. You have to enter a username."
        
    return HttpResponse(response)
    
    