from django.urls import path
from .. import views


urlpatterns = [
    
    # API POST/COMMENTS VIEWS:
    path('get/', views.GetCommentsAPIView.as_view(), name='get_all_comments'),
    path('review/<int:reviewId>/get/', views.GetCommentsForReviewAPIView.as_view(), name='get_all_comments_for_review'),
    path('parent/<int:parentId>/get/', views.GetCommentsForParentAPIView.as_view(), name='get_all_comments_for_parent'),
    path('<int:pk>/get/', views.GetSingleCommentAPIView.as_view(), name='get_comment'),
    path('post/', views.PostCommentAPIView.as_view(), name='post_comment'),
    path('<int:pk>/update/', views.UpdateCommentAPIView.as_view(), name='update_comment'),
    path('<int:pk>/delete/', views.DestroyCommentAPIView.as_view(), name='delete_comment'),
]