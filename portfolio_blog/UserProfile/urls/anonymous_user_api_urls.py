from django.urls import path
from .. import views


urlpatterns = [
    
    # API ANONYMOUS USER VIEWS:}
    
    path('get/', views.GetAnonymousUserAPIView.as_view(), name='get_all_anonymous_users'),
    path('<int:pk>/get/', views.GetSingleAnonymousUserAPIView.as_view(), name='get_anonymous_user'),
    path('register/', views.RegisterAnonymousUserAPIView.as_view(), name='register_anonymous_user'),
    path('<int:pk>/update/', views.UpdateAnonymousUserAPIView.as_view(), name='update_anonymous_user'),
    path('<int:pk>/delete/', views.DestroyAnonymousUserAPIView.as_view(), name='delete_anonymous_user'),
    
    
]
