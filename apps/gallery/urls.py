from django.urls import path
# from .gallery import views
from .views import GalleryIndex, Album

app_name = 'gallery'
urlpatterns = [
    path('',GalleryIndex.as_view(), name='photos'),
    path('album/<int:pk>/',Album.as_view(), name='album'),
]
