from django.urls import path
# from .gallery import views
from .views import GalleryIndex

app_name = 'gallery'
urlpatterns = [
    path('',GalleryIndex.as_view(), name='photos')
]
