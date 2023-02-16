from django.urls import path
from .. import views


urlpatterns = [
    
    # API USER VIEWS:}
    
    path('get/', views.GetUserAPIView.as_view(), name='get_all_users'),
    path('<int:pk>/get/', views.GetSingleUserAPIView.as_view(), name='get_user'),
    path('post/', views.PostUserAPIView.as_view(), name='post_user'),
    path('<int:pk>/update/', views.UpdateUserAPIView.as_view(), name='update_user'),
    path('<int:pk>/delete/', views.DestroyUserAPIView.as_view(), name='delete_user'),
    
    
]
