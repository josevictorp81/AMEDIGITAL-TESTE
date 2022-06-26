from django.urls import path

from . import views

urlpatterns = [
    path('create', views.PlanetCreateAPIView.as_view(), name='create-planet'),
    path('list', views.PlanetListView.as_view(), name='list-planet'),
]