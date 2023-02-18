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
from portfolio_blog.views import home, contact, about, resume
from django.conf.urls.static import static
from . import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
    path('about/', about, name="about"),
    path('resume/', resume, name="resume"),
    
    path('users/', include('UserProfile.urls.user_urls')),
    path('posts/', include('Post.urls.post_urls')),
    path('extras/', include('Extra.urls.extra_urls')),
    
    # API URLS
    
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
