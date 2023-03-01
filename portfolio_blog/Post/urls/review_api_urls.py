from django.urls import path
from .. import views


urlpatterns = [
    
    # API POST/REVIEW VIEWS:
    path('get/', views.GetReviewsAPIView.as_view(), name='get_all_reviews'),
    path('post/<int:postId>/get/', views.GetReviewsForPostAPIView.as_view(), name='get_all_reviews_for_post'),
    path('post/<int:postId>/user/<int:userId>/get/', views.GetUserReviewForPostAPIView.as_view(), name='get_user_review_for_post'),
    path('<int:pk>/get/', views.GetSingleReviewAPIView.as_view(), name='get_review'),
    path('post/', views.PostReviewAPIView.as_view(), name='post_review'),
    path('<int:pk>/update/', views.UpdateReviewAPIView.as_view(), name='update_review'),
    path('<int:pk>/delete/', views.DestroyReviewAPIView.as_view(), name='delete_review'),
]