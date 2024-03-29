from django.shortcuts import render
from .models import Gallery
from django.http import Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class GalleryIndex(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'
    context_object_name = 'gallery'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
class DetailAlbum(DetailView):
    model = Gallery
    template_name = 'gallery/album.html'
    context_object_name = 'album'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        try:
            gallery = Gallery.objects.get(id = pk)
            filteredAlbum = Gallery.objects.filter(place_code = gallery.place_code)
            context['info_photo'] = filteredAlbum
            return context
        except gallery.DoesNotExist:
            raise Http404('Album dose not exist')