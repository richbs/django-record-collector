from django.test import TestCase
from recollect.models import Album, ClassicalAlbum, PopularAlbum


class RecollectTest(TestCase):

    def setUp(self):

        album = Album()
        album.name = "Harvest Moon"
        album.year = 1992
        album.save()

        cl = ClassicalAlbum()
        cl.name = "Mahler: Symphony No. 2 \"Resurrection\""
        cl.year = 1976
        cl.save()

        pop = PopularAlbum()
        pop.name = "Help!"
        pop.year = 1965
        pop.save()

    def test_home(self):

        response = self.client.get('/')
        self.assertContains(response, 'Harvest', 1, 200)
        self.assertContains(response, '<li', 3, 200)

#     def test_albums(self):
#
#         response = self.client.get('/albums')
#         self.assertContains(response, "Harvest", 1, 200)
