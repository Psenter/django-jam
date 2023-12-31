"""
URL configuration for jamming_jango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers
from quickstart import views

#handles my routes and requests to routes
router = routers.DefaultRouter()
router.register(r'songs', views.SongViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'genre', views.GenreViewSet)
router.register(r'album', views.AlbumViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #what includes my generated URLs from the router
    path('', include(router.urls)),
    #allows users to access the API interface
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
