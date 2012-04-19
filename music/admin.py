from django.contrib import admin
from music.models import Album, Role, Performance, Work, Venue, Instrument

class AlbumAdmin(admin.ModelAdmin):
    pass

admin.site.register(Album, AlbumAdmin)

