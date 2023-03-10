from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.mainapp.urls'), name='mainapp'),
    path('gallery/',include('apps.gallery.urls'), name='gallery'),
]
