from django.test import TestCase
from recollect.models import Album, ClassicalAlbum, PopularAlbum, \
    Artist, Instrument, Role, Performance, Work


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

        don_plays = Role()
        don_plays.artist = don
        don_plays.save()

        sax = Instrument()
        sax.name = "Alto Saxophone"
        sax.save()

        cornet = Instrument()
        cornet.name = "Cornet"
        cornet.save()

        ornette_plays = Role()
        ornette_plays.artist = ornette
        ornette_plays.save()

        pop.artists.add(ornette_plays)

        ornette_plays.instruments.add(sax)
        don_plays.instruments.add(cornet)

        count = 0
        for t in ["Lonely Woman", "Eventually"]:
            count += 1
            w = Work(title=t)
            w.save()
            p = Performance(work=w, number=count, year=pop.year)
            p.save()
            pop.tracks.add(p)
            p.performers.add(ornette_plays)
            p.performers.add(don_plays)

    def test_home(self):

        response = self.client.get('/')
        self.assertContains(response, 'Harvest', 1, 200)
        self.assertContains(response, '<li', 3, 200)

    def test_album(self):

        response = self.client.get('/album/3-the-shape-of-jazz-to-come-1959')
        self.assertContains(response, 'Shape of Jazz', 1, 200)
        self.assertContains(response, 'Saxophone', 3, 200)
        self.assertContains(response, 'Don Cherry (Cornet)', 2, 200)
        self.assertContains(response, 'Eventually', 1, 200)
        self.assertContains(response, 'Lonely Woman', 1, 200)

    def test_albums(self):

        response = self.client.get('/albums')
        self.assertContains(response, "Harvest", 1, 200)
