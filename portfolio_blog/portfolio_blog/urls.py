"""portfolio_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
 
    
    # API URLS
    path('api/send_email/', views.send_email, name='send_email'),
    
    path('api/users/', include('UserProfile.urls.user_api_urls')),
    path('api/anonymous_users/', include('UserProfile.urls.anonymous_user_api_urls')),
    
    path('api/posts/', include('Post.urls.post_api_urls')),
    path('api/reviews/', include('Post.urls.review_api_urls')),
    path('api/comments/', include('Post.urls.comment_api_urls')),
    path('api/likes/', include('Post.urls.like_api_urls')),
    
    path('api/technologies/', include('Extra.urls.technologies_api_urls')),
    path('api/studies/', include('Extra.urls.studies_api_urls')),
    path('api/validations/', include('Extra.urls.validations_api_urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
