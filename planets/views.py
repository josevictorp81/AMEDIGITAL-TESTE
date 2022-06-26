from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
import requests

from .serializers import PlanetSerializer
from .models import Planet

class PlanetCreateAPIView(CreateAPIView):
    queryset = Planet.objects.last()
    serializer_class = PlanetSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        name = request.data['name']
        quantity = 0
        req = requests.get(f'https://swapi.dev/api/planets?search={name}').json()
        res = req['results']
        if res:
            quantity = len(req['results'][0]['films'])
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(films_apparitions=quantity)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanetListView(ListAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

