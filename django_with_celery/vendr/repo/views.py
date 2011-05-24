from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.servers.basehttp import FileWrapper
from repo.models import RepoFile
from repo.forms import UploadFileForm
import os
import uuid

def handle_upload(f, uuid):
    if not os.path.exists(settings.UPLOADS_DIR):
        os.makedirs(settings.UPLOADS_DIR)
    dest = open(os.path.join(settings.UPLOADS_DIR, uuid), 'wb+')
    for c in f.chunks():
        dest.write(c)
    dest.close()

def index(request):
    form = UploadFileForm(initial={'uuid': str(uuid.uuid4())})
    vars = RequestContext(request, {
        'form': form,
    })
    return render_to_response('index.html', vars)

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            repo_file = RepoFile()
            repo_file.uuid = form.cleaned_data['uuid']
            repo_file.filename = request.FILES['filename']
            repo_file.save()
            handle_upload(request.FILES['filename'], form.cleaned_data['uuid'])
        vars = RequestContext(request, {
            'host': request.get_host(),
            'link': reverse('repo.views.download', args=[form.cleaned_data['uuid']]),
            'max_file_age': settings.MAX_FILE_AGE,
        })
        return render_to_response('show_link.html', vars)
    else:
        return HttpResponseRedirect('/')

def download(request, file_id):
    try:
        repo_file = RepoFile.objects.get(uuid=file_id)
        repo_file.download_count += 1
        repo_file.save()
        # use filewrapper to transfer large files faster/better
        fname = os.path.join(settings.UPLOADS_DIR, file_id)
        wrapper = FileWrapper(file(fname))
        response = HttpResponse(wrapper, content_type='application/octet-stream')
        response['Content-Length'] = os.path.getsize(fname)
        response['Content-Disposition'] = 'attachment; filename=\"{0}\"'.format(repo_file.filename)
        return response
    except:
        vars = RequestContext(request, {
        })
        return render_to_response('unknown.html', vars)

