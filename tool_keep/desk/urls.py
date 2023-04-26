from django.urls import path

from . import views


app_name = 'desk'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.user_info),
]
