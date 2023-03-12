from django.urls import path
from .. import views


urlpatterns = [

    # API EXTRA/VALIDATION VIEWS:
    path('get/', views.GetValidationsAPIView.as_view(), name='get_all_validations'),
    path('<int:pk>/get/', views.GetSingleValidationAPIView.as_view(), name='get_validation'),
    path('post/', views.PostValidationAPIView.as_view(), name='post_validation'),
    path('<int:pk>/update/', views.UpdateValidationAPIView.as_view(), name='update_validation'),
    path('<int:pk>/delete/', views.DestroyValidationAPIView.as_view(), name='delete_validation'),
    
    # Get user/anon validation for a Technology
    path('technology/<int:skillId>/anonymous_user/<str:identifier>/get/', views.GetAnonUserValidationForTechnologyAPIView.as_view(), name='get_anon_user_validation_for_technology'),
    path('technology/<int:skillId>/user/<int:identifier>/get/', views.GetUserValidationForTechnologyAPIView.as_view(), name='get_user_validation_for_technology'),
    # Get user/anon validation for a Study
    path('study/<int:studyId>/anonymous_user/<str:identifier>/get/', views.GetAnonUserValidationForStudyAPIView.as_view(), name='get_anon_user_validation_for_study'),
    path('study/<int:studyId>/user/<int:identifier>/get/', views.GetUserValidationForStudyAPIView.as_view(), name='get_user_validation_for_study'),
]