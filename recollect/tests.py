from django.test import TestCase
from recollect.models import Album, ClassicalAlbum, PopularAlbum, \
                            Artist, Role, AlbumArtist


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
        pop.name = "The Shape of Jazz to Come"
        pop.year = 1959
        pop.save()

        ornette = Artist()
        ornette.name = "Ornette Coleman"
        ornette.surname = "Coleman"
        ornette.given_name = "Ornette"
        ornette.save()

        ornette_plays = AlbumArtist()
        ornette_plays.artist = ornette
        ornette_plays.album = pop
        ornette_plays.save()


    def test_home(self):

        response = self.client.get('/')
        self.assertContains(response, 'Harvest', 1, 200)
        self.assertContains(response, '<li', 3, 200)

#     def test_albums(self):
#
#         response = self.client.get('/albums')
#         self.assertContains(response, "Harvest", 1, 200)
