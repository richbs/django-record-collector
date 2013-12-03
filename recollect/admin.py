from django.contrib import admin
from recollect.models import Album, Role, Label, \
    Performance, Work, Venue, Instrument


class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class LabelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class InstrumentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Album, AlbumAdmin)
admin.site.register(Label, LabelAdmin)
admin.site.register(Instrument, InstrumentAdmin)
