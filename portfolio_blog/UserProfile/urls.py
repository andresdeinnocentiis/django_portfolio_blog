from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all_users, name='all_profiles'),
    path('register/', views.register_user, name='register_user'),
    path('<str:username>/', views.get_user_profile, name='user_profile'),
    
]
