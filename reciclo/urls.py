"""reciclo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from trashcan.views import TrashCanViewSet, LevelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('trash-cans', TrashCanViewSet)
router.register('levels', LevelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    #Trashcan
    path('cans/', include('trashcan.urls', namespace='trashcan_app')),
    #Home
    path('', include('home.urls', namespace='home_app')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_app')),
    path('api/', include(router.urls)),



]
