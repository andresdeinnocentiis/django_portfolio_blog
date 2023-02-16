from django.urls import path
from .. import views


urlpatterns = [
    #path('', views.get_all_posts, name='all_posts'),
    #path('<int:pk>/', views.get_post, name='post'),
    #path('create/', views.add_post, name='add_post'),
    
    # API VIEWS:
    #path('get/', views.GetPostAPIView.as_view(), name='get_all_posts'),
    #path('<int:id>/get/', views.GetSinglePostAPIView.as_view(), name='get_post'),
    #path('post/', views.PostPostAPIView.as_view(), name='post_post'),
    #path('<int:pk>/update/', views.UpdatePostAPIView.as_view(), name='update_post'),
    #path('<int:pk>/delete/', views.DestroyPostAPIView.as_view(), name='delete_post'),
]