"""school_co URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
import djoser

from base.urls import router as base_router
from school_co.urls import router as school_co_router

router = routers.DefaultRouter()
router.registry.extend(base_router.registry)
router.registry.extend(school_co_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls, 'admin'),
    path('', include('base.urls')),
    path('', include('school_co.urls')),
    path('api/', include(router.urls)),
    path('api/auth/', include('rest_framework.urls')),
    # path to djoser end points - потом можно поменять на 'api/auth/'
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    # path to our account's app endpoints
    path("api/accounts/", include("accounts.urls")),
    path('register', 'registration_teacher_view'), #registration form
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
