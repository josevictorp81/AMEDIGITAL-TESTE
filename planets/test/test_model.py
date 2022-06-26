from rest_framework.test import APIClient, APITestCase

from planets.models import Planet

class PlanetTestModel(APITestCase):
    def test_planet_str(self):
        planet = Planet.objects.create(name='nametest', climate='climatetest', terrain='terraintest', films_apparitions=3)

        self.assertEqual(planet.__str__(), 'nametest')
