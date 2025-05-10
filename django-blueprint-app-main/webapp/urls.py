"""
URL configuration for webapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from forum import views as forum_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls), # default, part of django
    path('', include('main.urls')),
    path('news/', include('news.urls')), 
    path('forum/<str:kolo_slug>/', forum_views.kolo_forum, name='kolo_forum'),
    #path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # ✅ This fixes the 404

    #path('forum/', include('forum.urls')) #delegating authority to an internal application to forum.urls that is needed to be created
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
