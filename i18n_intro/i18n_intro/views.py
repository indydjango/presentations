from django.http import HttpResponse
from django.utils.translation import ugettext as _

def index(request):
    response = _("Hello, world")
    return HttpResponse(response + '\n')

