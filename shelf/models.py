from django.db import models

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
        return u"%s" % (name)

class Work(models.Model):
    """
    Either a classical opus or a track on an album
    """
    title = models.CharField(blank=False, max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    opus_number = models.CharField(blank=True, max_length=10)
    composers = models.ManyToManyField(Artist, through="Role")
    year_composed = models.IntegerField(blank=True, null=True)
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"Track"

    
class Performance(models.Model):
    """
    A performance of a work given at a particular date and time
    Could be a recording date
    """
    year = models.IntegerField(blank=True)
    date = models.DateField()
    venue = models.ForeignKey(Venue)
    work = models.ForeignKey(Work)
    performers = models.ManyToManyField(Artist, through="Role")

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"%s %d" % (self.work, self.year)


class Instrument(models.Model):
    """(Instrument description)"""
    
    name = models.CharField(blank=True, max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"Instrument"


class Role(models.Model):
    artist = models.ForeignKey(Artist)
    work = models.ForeignKey(Work)
    performance = models.ForeignKey(Performance)
    instruments = models.ManyToManyField(Instrument)
    composer = models.BooleanField(default=False)
    performer = models.BooleanField(default=True)


class Album(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    performances = models.ManyToManyField(Performance)
    release_date = models.DateField()
    year = models.IntegerField(blank=True, null=True)
    