from django.test import TestCase
from recollect.models import Album


class RecollectTest(TestCase):

    def setUp(self):
        album = Album()
        album.name = "Harvest Moons"
        album.year = 1990
        album.save()

    def test_home(self):

        response = self.client.get('/')
        self.assertContains(response, 'world', 1, 200)

#     def test_albums(self):
#
#         response = self.client.get('/albums')
#         self.assertContains(response, "Harvest", 1, 200)
