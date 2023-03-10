from django.urls import path
# from .gallery import views
from .views import GalleryIndex

urlpatterns = [
    path('',GalleryIndex.as_view(), name='gallery')
]
