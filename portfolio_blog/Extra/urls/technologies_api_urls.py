from django.urls import path
from .. import views


urlpatterns = [

    # API EXTRA/TECHNOLOGY VIEWS:
    path('get/', views.GetTechnologyAPIView.as_view(), name='get_all_technologies'),
    path('<int:pk>/get/', views.GetSingleTechnologyAPIView.as_view(), name='get_technology'),
    path('post/', views.PostTechnologyAPIView.as_view(), name='post_technology'),
    path('<int:pk>/update/', views.UpdateTechnologyAPIView.as_view(), name='update_technology'),
    path('<int:pk>/delete/', views.DestroyTechnologyAPIView.as_view(), name='delete_technology'),
]