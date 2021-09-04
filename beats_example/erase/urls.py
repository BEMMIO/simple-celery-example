from django.urls import path

from . import views

app_name = 'erase'

urlpatterns = [
    path('', views.index,name='index'),
]
