from django.urls import path

from . import views

urlpatterns = [
    path('create', views.PlanetCreateAPIView.as_view(), name='create-planet'),
]