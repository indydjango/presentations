from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return HttpResponse('Hello world...')

def exception_test(request):
    1 / 0
    return HttpResponse('Never gets here')

def test_404(request):
    raise Http404()

def template_exc_test(request):
    context = {
        'name': 'foo',
    }
    return render_to_response('foo.html', context_instance=RequestContext(request))