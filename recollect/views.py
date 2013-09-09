# Create your views here.
from django.http import HttpResponse
from recollect.models import Album
from django.template import RequestContext, loader


def home(request):

    albums = Album.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {'albums': albums})

    return HttpResponse(template.render(context))

def albums(request):

    pass

def album(request, album_slug):

    album = Album.objects.get(slug=album_slug)
    template = loader.get_template('album.html')
    context = RequestContext(request, {'album': album})
    return HttpResponse(template.render(context))
