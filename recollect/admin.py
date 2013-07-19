from django.contrib import admin
from recollect.models import Album, Role, Performance, Work, Venue, Instrument

class AlbumAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Album, AlbumAdmin)

