from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def home(request):    
    if request.method == 'POST':
        form = UploadPhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            request.session['id_photo'] = form.model
            return redirect('result')
    else:
        form = UploadPhotoForm()
    return render(request, 'home.html', {'form' : form})

def result(request):
    context = {}
    return render(request, 'result.html', context)
