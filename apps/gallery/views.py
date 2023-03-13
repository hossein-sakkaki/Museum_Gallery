from django.shortcuts import render
from django.views import View
from .models import Gallery


# Create your views here.

# class GalleryIndex(View):
#     model = Gallery
#     template_name = 'gallery/gallery.html'
#     context_object_name = 'gallery'
    
#     def get(self, request, *args, **kwargs):
#         context = {
#             'hello': Gallery
#         }
#         return render(request, 'gallery/gallery.html', context)





from django.views.generic.list import ListView
class GalleryIndex(ListView):
    model = Gallery
    template_name = 'gallery/gallery.html'
    context_object_name = 'gallery'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class Album(ListView):
    model = Gallery
    template_name = 'gallery/album.html'