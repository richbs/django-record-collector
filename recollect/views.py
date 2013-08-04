# Create your views here.
from django.http import HttpResponse
from recollect.models import Album
from django.template import RequestContext, loader


def home(request):

    albums = Album.objects.all()
    template = loader.get_template('index.html')
    context = RequestContext(request, {'albums': albums})

    return HttpResponse(template.render(context))
