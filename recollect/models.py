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
    composers = models.ManyToManyField(Artist)
    year_composed = models.IntegerField(blank=True, null=True)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"%s" % (self.title)


class Instrument(models.Model):
    """
    A musical device played by an artist
    """

    name = models.CharField(blank=True, max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return self.name


class Performance(models.Model):
    """
    A performance of a work given at a particular date and time
    Could be a recording date
    """
    number = models.IntegerField(null=True, db_index=True)
    year = models.IntegerField(blank=True)
    date = models.DateField(null=True)
    venue = models.ForeignKey(Venue, null=True)
    work = models.ForeignKey(Work)
    performers = models.ManyToManyField("Role")

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        roles = [unicode(r) for r in self.performers.all()]
        artists = ", ".join(roles)
        return u"%s (%d) (%s)" % (self.work, self.year, artists)


class Role(models.Model):
    """
    Links performances to artists
    """
    artist = models.ForeignKey(Artist)
    instruments = models.ManyToManyField(Instrument)

    def __unicode__(self):

        return self.artist.name


class Label(models.Model):
    """
    The record label publishing this record
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)

    def __unicode__(self):
        return u"%s" % (self.name)


class Album(models.Model):
    """
    A record
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    release_date = models.DateField(null=True)
    year = models.IntegerField(blank=True, null=True)
    label = models.ForeignKey(Label, blank=True, null=True)
    artists = models.ManyToManyField(Role)

    def __unicode__(self):
        roles = [unicode(r) for r in self.artists.all()]
        artists = ", ".join(roles)
        return u"%s (%d) by %s" % (self.name, self.year, artists)

    def get_slug(self):

        return slugify(u"%d %s %d" % (self.id, self.name, self.year))


class ClassicalAlbum(Album):
    """
    Wraps the album for classical performances
    """
    performances = models.ManyToManyField(Performance)


class PopularAlbum(Album):
    """
    Wraps the album to link performances as tracks
    """
    tracks = models.ManyToManyField(Performance)
