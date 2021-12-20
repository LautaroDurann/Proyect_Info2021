from django.contrib import admin
from django.urls import path
from django.conf.urls import include, path

urlpatterns = [
    path('posts/', include('apps.posts.urls')),
    path('admin/', admin.site.urls),
]
