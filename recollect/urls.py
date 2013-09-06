from django.conf.urls import patterns, url
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'recollect.views.home', name='home'),
    url(r'^albums$', 'recollect.views.albums', name='albums'),
)
