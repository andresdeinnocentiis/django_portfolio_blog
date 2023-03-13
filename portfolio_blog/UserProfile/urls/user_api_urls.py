from django.urls import path
from .. import views


urlpatterns = [
    
    # API USER VIEWS:}
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'), # URL PARA GENERAR EL JWT TOKEN DEL USUARIO
    path('register/', views.registerUser, name='register_user'),
    path('username_exists/', views.username_exists, name='username_exists'), # URL PARA GENERAR EL JWT TOKEN DEL USUARIO
    path('email_exists/', views.email_exists, name='email_exists'),
    path('get/', views.GetUserAPIView.as_view(), name='get_all_users'),
    path('<int:pk>/get/', views.GetSingleUserAPIView.as_view(), name='get_user'),
    path('<int:pk>/update/', views.UpdateUserAPIView.as_view(), name='update_user'),
    path('<int:pk>/delete/', views.DestroyUserAPIView.as_view(), name='delete_user'),
    
    
]
