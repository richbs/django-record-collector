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
        cl.year = 1968
        cl.save()

        pop = PopularAlbum()
        pop.name = "The Shape of Jazz to Come"
        pop.year = 1959
        pop.save()

        haitink = Artist()
        haitink.name = "Bernard Haitink"
        haitink.surname = "Haitink"
        haitink.given_name = "Bernard"
        haitink.save()
        haitink.album_set.add(cl)

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

        pop.artists.add(ornette)

        neil = Artist()
        neil.name = "Neil Young"
        neil.surname = "Young"
        neil.given_name = "Neil"
        neil.save()

        neil.album_set.add(album)

        sax = Instrument()
        sax.name = "Alto Saxophone"
        sax.save()

        cornet = Instrument()
        cornet.name = "Cornet"
        cornet.save()

        conducting = Instrument()
        conducting.name = "Conductor"
        conducting.save()

        count = 0
        for t in ["Lonely Woman", "Eventually"]:
            count += 1
            w = Work(title=t)
            w.save()
            p = Performance(work=w, number=count, year=pop.year)
            p.save()
            pop.tracks.add(p)

            r1 = Role(performance=p, artist=don)
            r1.save()
            r1.instruments.add(cornet)
            r2 = Role(performance=p, artist=ornette)
            r2.save()
            r2.instruments.add(sax)

    def test_home(self):

        response = self.client.get('/')
        self.assertContains(response, 'Harvest', 1, 200)
        self.assertContains(response, '<li', 3, 200)

    def test_album(self):

        response = self.client.get('/album/3-the-shape-of-jazz-to-come-1959')
        self.assertContains(response, 'Shape of Jazz', 1, 200)
        self.assertContains(response, 'Saxophone', 2, 200)
        self.assertContains(response, 'Don Cherry (Cornet)', 2, 200)
        self.assertContains(response, 'Eventually', 1, 200)
        self.assertContains(response, 'Lonely Woman', 1, 200)

    def test_albums(self):

        response = self.client.get('/albums')
        self.assertContains(response, "Harvest", 1, 200)
