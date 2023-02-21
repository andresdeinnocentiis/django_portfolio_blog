from django.urls import path
from .. import views


urlpatterns = [

    # API EXTRA/STUDY VIEWS:
    path('get/', views.GetStudysAPIView.as_view(), name='get_all_studies'),
    path('<int:pk>/get/', views.GetSingleStudyAPIView.as_view(), name='get_study'),
    path('post/', views.PostStudyAPIView.as_view(), name='post_study'),
    path('<int:pk>/update/', views.UpdateStudyAPIView.as_view(), name='update_study'),
    path('<int:pk>/delete/', views.DestroyStudyAPIView.as_view(), name='delete_study'),
]