from django.urls import path
from apps.mainapp import views

app_name = 'mainapp'
urlpatterns = [
    path('',views.Index, name='index'),
]
