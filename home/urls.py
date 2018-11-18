from django.urls import path
from .views import HomeViews, LogInViews, SignUpViews, LogOutViews

app_name = 'home_app'


urlpatterns = [
    path('',HomeViews.as_view(),name = 'home',),
    path('login/',LogInViews.as_view(),name = 'login',),
    path('signup/',SignUpViews.as_view(),name = 'signup',),
    path('logout/',LogOutViews.as_view(),name = 'logout',),
]