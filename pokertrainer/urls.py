"""
URL configuration for pokertrainer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from . import views
from users import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # BASIC - basic routing
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),

    # USER AUTHENTICATION - routes to views.py in users
    path('signup/', auth_views.join),
    path('login/', auth_views.user_login),
    path('logout/', auth_views.user_logout),

    # APPS - routes to urls.py in their apps folder
    path('lessons/', include('lessons.urls')),
    path('trainer/', include('trainer.urls')),
    path('famous/', include('famous.urls')),
]
