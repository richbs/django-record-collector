from django.db import models

class Venue(models.Model):
    """
    A recording venue or live gig
    e.g. Carnegie Hall, Abbey Road Studios
    """
    name = models.CharField(blank=False, max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"%s" % (self.name)


class Performance(models.Model):
    """
    A performance of a work given at a particular date and time
    Could be a recording date
    """
    year = models.IntegerField(blank=True)
    date = models.DateField()
    venue = models.ForeignKey(Venue)

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"Performance"


class Work(models.Model):
    """
    Either a classical opus or a track on an album
    """

    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"Track"


class Performer(models.Model):
    """
    
    """
    
    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __unicode__(self):
        return u"Artist"

class Album(models.Model):

    name = models.CharField(max_length=255)
    performances = models.ManyToManyField(Performance)
