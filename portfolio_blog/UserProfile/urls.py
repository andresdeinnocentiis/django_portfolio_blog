from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_all_users, name='all_users'),
    path('register/', views.register_user, name='register_user'),
    path('<int:id>/', views.get_user, name='get_user'),
    path('search/', views.search_user, name='search_user'),
    path('search/result/', views.search_user_result, name='search_user_result'),
    
    
]
