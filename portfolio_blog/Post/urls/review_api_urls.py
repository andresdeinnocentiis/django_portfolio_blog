from django.urls import path
from .. import views


urlpatterns = [
    
    # API POST/REVIEW VIEWS:
    path('get/', views.GetReviewAPIView.as_view(), name='get_all_reviews'),
    path('<int:pk>/get/', views.GetSingleReviewAPIView.as_view(), name='get_review'),
    path('post/', views.PostReviewAPIView.as_view(), name='post_review'),
    path('<int:pk>/update/', views.UpdateReviewAPIView.as_view(), name='update_review'),
    path('<int:pk>/delete/', views.DestroyReviewAPIView.as_view(), name='delete_review'),
]