from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from web_project.settings import MEDIA_ROOT
from .forms import *
from .models import *

import os

# Create your views here.
def home(request):
    # Delete photos
    photosdir = os.path.join(MEDIA_ROOT, 'photos')
    for dir in os.listdir(photosdir):
        os.remove(os.path.join(photosdir, dir))
    # Delete photo objects
    UploadedPhoto.objects.all().delete()

    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            photo = UploadedPhoto.objects.last()
            request.session['url'] = photo.photo.url
            return redirect('result')
        # TODO: Print an error if form is not valid.
        # TODO: Make the photo have a size requirement.
        # TODO: Turn the photo B&W / resize if necessary for processing.
    else:
        form = UploadPhotoForm()
    return render(request, 'home.html', {'form' : form})

def result(request):
    context = {}
    if('url' in request.session):
        context['url'] = request.session['url']
        del request.session['url']

    return render(request, 'result.html', context)
