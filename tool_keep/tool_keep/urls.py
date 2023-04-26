from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('desk.urls', namespace='desk')),
    path('admin/', admin.site.urls),
]
