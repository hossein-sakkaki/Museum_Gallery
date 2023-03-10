from django.urls import path
from apps.mainapp import views

urlpatterns = [
    path('',views.Index, name='index')
]
