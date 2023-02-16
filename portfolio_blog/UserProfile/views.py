from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile
from .forms import UserRegisterForm
from django.http import HttpResponse

# Django REST Framework imports:
from .serializers import UserProfileSerializer, AnonymousUserSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

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
                username= info['username'].lower(),
                email= info['email'].lower(),
                password= info['password'],
                first_name= info['first_name'].capitalize(),
                last_name= info['last_name'].capitalize(),
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
    

# API USER VIEWS:
class GetUserAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the blog Users.
    '''
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class GetSingleUserAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single blog User.
    '''
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        '''
        Sobrescribimos la función `get_queryset` para poder filtrar el request 
        por medio de la url. En este caso traemos de la url por medio de `self.kwargs` 
        el parámetro `User_id` y con él realizamos una query para traer 
        el User del ID solicitado.  
        '''
        try:
            id = self.kwargs['id']
            queryset = User.objects.filter(id=id)
            return queryset
        
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        
class PostUserAPIView(CreateAPIView):
    __doc__ = f'''
    `[POST]`
    This API view inserts a blog post on the DataBase.
    '''
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class UpdateUserAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a blog User.
    '''
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class DestroyUserAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view updates a blog User.
    '''
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsAdminUser] 