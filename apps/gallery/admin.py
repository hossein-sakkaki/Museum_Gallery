from django.contrib import admin
from .models import Gallery
# Register your models here.

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['place_code', 'shot_photo_date', 'image_name', 'text_info', 'parent_code', 'is_active']
    list_filter = ['place_code', 'is_active']
    search_fields = ['place_code', 'text_info']
    prepopulated_fields = {'slug': ('place_name','image_name')}