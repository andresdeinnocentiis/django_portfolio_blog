from django.urls import path
from .. import views


urlpatterns = [

    # API EXTRA/VALIDATION VIEWS:
    path('get/', views.GetValidationAPIView.as_view(), name='get_all_validations'),
    path('<int:pk>/get/', views.GetSingleValidationAPIView.as_view(), name='get_validation'),
    path('post/', views.PostValidationAPIView.as_view(), name='post_validation'),
    path('<int:pk>/update/', views.UpdateValidationAPIView.as_view(), name='update_validation'),
    path('<int:pk>/delete/', views.DestroyValidationAPIView.as_view(), name='delete_validation'),
]