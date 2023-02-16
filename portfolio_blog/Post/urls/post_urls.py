from django.urls import path
from .. import views


urlpatterns = [
    path('', views.get_all_posts, name='all_posts'),
    path('<int:pk>/', views.get_post, name='post'),
    path('create/', views.add_post, name='add_post'),
    
]
