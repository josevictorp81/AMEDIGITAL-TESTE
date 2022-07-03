from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
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
        else:
            return Response(data={'detail': 'This planet do not exists in star wars universe!'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(films_apparitions=quantity)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlanetListView(ListAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

    def get(self, request, *args, **kwargs):
        name = request.query_params.get('name')
        if name is not None:
            queryset = self.queryset.filter(name__icontains=name)
            serializer = PlanetSerializer(queryset, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return super().get(request, *args, **kwargs)


class PlanetaRetrieveView(RetrieveAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer


class PlanetDestroyView(DestroyAPIView):
    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
