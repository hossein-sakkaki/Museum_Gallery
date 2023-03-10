from django.shortcuts import render
from django.conf import settings

def media_admin(request):
    return {'media_url': settings.MEDIA_URL}

# Create your views here.
def Index(request):
    return render(request, 'mainapp/index.html')
