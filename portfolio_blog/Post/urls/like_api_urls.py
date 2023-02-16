from django.urls import path
from .. import views


urlpatterns = [
    
    # API POST/LIKE VIEWS:
    path('get/', views.GetLikeAPIView.as_view(), name='get_all_likes'),
    path('<int:pk>/get/', views.GetSingleLikeAPIView.as_view(), name='get_like'),
    path('post/', views.PostLikeAPIView.as_view(), name='post_like'),
    path('<int:pk>/update/', views.UpdateLikeAPIView.as_view(), name='update_like'),
    path('<int:pk>/delete/', views.DestroyLikeAPIView.as_view(), name='delete_like'),
]