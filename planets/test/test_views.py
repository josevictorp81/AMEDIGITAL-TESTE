from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse

from planets.models import Planet
from planets.serializers import PlanetSerializer

CREATE_PLANET = reverse('create-planet')
LIST_PLANET = reverse('list-planet')

def planet_view(path, planet_id):
    return reverse(path, args=[planet_id])


class TestView(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
    
    def test_create_planet_inexists(self):
        payload = {'name': 'nametest', 'climate': 'climatetest', 'terrain': 'terraintest'}

        res = self.client.post(CREATE_PLANET ,payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_planet_exists(self):
        payload = {'name': 'Tatooine', 'climate': 'arid', 'terrain': 'desert'}

        res = self.client.post(CREATE_PLANET ,payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    def test_create_planet_invalid(self):
        payload = {'name': '', 'climate': 'arid', 'terrain': 'desert'}

        res = self.client.post(CREATE_PLANET ,payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_list_planets(self):
        Planet.objects.create(name='nametest', climate='climatetest', terrain='terraintest')
        Planet.objects.create(name='test', climate='climatetest1', terrain='terraintest1', films_apparitions=3)

        res = self.client.get(LIST_PLANET)

        planets = Planet.objects.all()
        serializer = PlanetSerializer(planets, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_filter_planets_by_name(self):
        Planet.objects.create(name='nametest', climate='climatetest', terrain='terraintest')
        Planet.objects.create(name='test', climate='climatetest1', terrain='terraintest1', films_apparitions=3)

        res = self.client.get('http://127.0.0.1:8000/api/planets/list?name=nametest')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
    
    def test_list_planet_id(self):
        planet = Planet.objects.create(name='nametest', climate='climatetest', terrain='terraintest')
        Planet.objects.create(name='test', climate='climatetest1', terrain='terraintest1', films_apparitions=3)

        url = planet_view('list-planet-id', planet.id)
        res = self.client.get(url)
        serializer = PlanetSerializer(planet)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
    
    def test_delete_planet(self):
        planet = Planet.objects.create(name='nametest', climate='climatetest', terrain='terraintest')

        url = planet_view('delete-planet', planet.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
