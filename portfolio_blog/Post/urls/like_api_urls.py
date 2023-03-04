from django.urls import path
from .. import views


urlpatterns = [
    
    # API POST/LIKE VIEWS:
    path('get/', views.GetLikesAPIView.as_view(), name='get_all_likes'),
    path('post/<int:postId>/anonymous_user/<str:identifier>/get/', views.GetAnonUserLikeForPostAPIView.as_view(), name='get_anon_user_like_for_post'),
    path('post/<int:postId>/user/<int:identifier>/get/', views.GetUserLikeForPostAPIView.as_view(), name='get_user_like_for_post'),
    path('review/<int:reviewId>/anonymous_user/<str:identifier>/get/', views.GetAnonUserLikeForReviewAPIView.as_view(), name='get_anon_user_like_for_review'),
    path('review/<int:reviewId>/user/<int:identifier>/get/', views.GetUserLikeForReviewAPIView.as_view(), name='get_user_like_for_review'),
    path('<int:pk>/get/', views.GetSingleLikeAPIView.as_view(), name='get_like'),
    path('post/', views.PostLikeAPIView.as_view(), name='post_like'),
    path('<int:pk>/update/', views.UpdateLikeAPIView.as_view(), name='update_like'),
    path('<int:pk>/delete/', views.DestroyLikeAPIView.as_view(), name='delete_like'),
]