from django.urls import path
from . import views
from .views import CreateView, ListView

app_name = 'main_app'


urlpatterns = [
    path('', views.my_view,name = 'can-list',),
    path('crear/', CreateView.as_view(),name = 'can-create',),
    path('<int:pk>/', ListView.as_view(),name = 'can-detail',),
    #path('<int:id>/', views.my_view_detail,name = 'can-detail',),
]
