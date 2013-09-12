from django.test import TestCase
from recollect.models import Album, ClassicalAlbum, PopularAlbum, \
                            Artist, AlbumArtist, Instrument, Track


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
        pop.slug = pop.get_slug()
        pop.save()

        ornette = Artist()
        ornette.name = "Ornette Coleman"
        ornette.surname = "Coleman"
        ornette.given_name = "Ornette"
        ornette.save()

        don = Artist()
        don.name = "Don Cherry"
        don.surname = "Cherry"
        don.given_name = "Don"
        don.save()


        don_plays = AlbumArtist()
        don_plays.artist = don
        don_plays.album = pop
        don_plays.save()

        sax = Instrument()
        sax.name = "Alto Saxophone"
        sax.save()

        cornet = Instrument()
        cornet.name = "Cornet"
        cornet.save()


        ornette_plays = AlbumArtist()
        ornette_plays.artist = ornette
        ornette_plays.album = pop
        ornette_plays.save()
        ornette_plays.instruments.add(sax)
        don_plays.instruments.add(cornet)

        track1 = Track()
        track1.number = 1
        track1.title = "Lonely Woman"
        track1.save()


        track2 = Track()
        track2.number = 2
        track2.title = "Eventually"
        track2.save()

        pop.tracks.add(track1)
        pop.tracks.add(track2)

    def test_home(self):

        response = self.client.get('/')
        self.assertContains(response, 'Harvest', 1, 200)
        self.assertContains(response, '<li', 3, 200)

    def test_album(self):

        response = self.client.get('/album/3-the-shape-of-jazz-to-come-1959')
        self.assertContains(response, 'Shape of Jazz', 1, 200)
        self.assertContains(response, 'Saxophone', 1, 200)
        self.assertContains(response, 'Don Cherry (Cornet)', 1, 200)
        self.assertContains(response, 'Eventually', 1, 200)
        self.assertContains(response, 'Lonely Woman', 1, 200)

#     def test_albums(self):
#
#         response = self.client.get('/albums')
#         self.assertContains(response, "Harvest", 1, 200)
