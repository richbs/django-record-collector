from django.db import models
from django.utils.text import slugify


class Venue(models.Model):
    """
    A recording venue or live gig
    e.g. Carnegie Hall, Abbey Road Studios
    """
    name = models.CharField(blank=False, max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"%s" % (self.name)


class Artist(models.Model):
    """
    Class for composers, artists, critics
    Duke Ellington is composer and performer
    """
    name = models.CharField(blank=True, max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    surname = models.CharField(blank=True, max_length=255)
    given_name = models.CharField(blank=True, max_length=255)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"%s" % (self.name)


class Work(models.Model):
    """
    Either a classical opus or a show tune or a standard
    or a track on an album
    """
    title = models.CharField(blank=False, max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    opus_number = models.CharField(blank=True, max_length=10)
    composers = models.ManyToManyField(Artist, through="Performing")
    year_composed = models.IntegerField(blank=True, null=True)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"%s" % (self.title)


class Track(Work):

    number = models.IntegerField(blank=True, null=False, db_index=True)
    artists = models.ManyToManyField(Artist, through="Playing")


class Instrument(models.Model):
    """(Instrument description)"""

    name = models.CharField(blank=True, max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"%s" (self.name)


class Performance(models.Model):
    """
    A performance of a work given at a particular date and time
    Could be a recording date
    """
    year = models.IntegerField(blank=True)
    date = models.DateField()
    venue = models.ForeignKey(Venue)
    work = models.ForeignKey(Work)
    performers = models.ManyToManyField(Artist, through="Performing")

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"%s %d" % (self.work, self.year)


class Role(models.Model):

    artist = models.ForeignKey(Artist)
    instruments = models.ManyToManyField(Instrument)
    composer = models.BooleanField(default=False)

    def __unicode__(self):
        return self.artist.name

class Playing(Role):
    track = models.ForeignKey(Track)


class Performing(Role):

    work = models.ForeignKey(Work)
    performance = models.ForeignKey(Performance, null=True)


class Label(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)


class Album(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    release_date = models.DateField(null=True)
    year = models.IntegerField(blank=True, null=True)
    label = models.ForeignKey(Label, blank=True, null=True)
    artists = models.ManyToManyField(Artist, through="AlbumArtist")

    def __unicode__(self):
        return u"%s (%d)" % (self.name, self.year)

    def get_slug(self):

        return slugify(u"%d %s %d" % (self.id,
                                     self.name,
                                     self.year))

class ClassicalAlbum(Album):

    performances = models.ManyToManyField(Performance)


class PopularAlbum(Album):

    tracks = models.ManyToManyField(Track)


class AlbumArtist(Role):

    album = models.ForeignKey(Album)
