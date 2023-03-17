from django.urls import path
from .views import GalleryIndex, DetailAlbum

app_name = 'gallery'
urlpatterns = [
    path('',GalleryIndex.as_view(), name='photos'),
    path('album/<int:pk>',DetailAlbum.as_view(), name='album'),
]
