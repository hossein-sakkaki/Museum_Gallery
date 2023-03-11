from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.mainapp.urls',namespace='mainapp'), name='mainapp'),
    path('gallery/',include('apps.gallery.urls',namespace='gallery'), name='gallery'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
