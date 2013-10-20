from django.conf.urls import patterns, url
urlpatterns = patterns('',
    url(r'^$', 'recollect.views.home', name='home'),
    url(r'^albums$', 'recollect.views.albums', name='albums'),
    url(r'^album/(?P<album_slug>[A-z0-9-]+)$', 'recollect.views.album', name='album'),
)
