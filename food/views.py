from django.shortcuts import render, redirect
from .forms import UploadFileForm

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def result(request):
    return render(request, 'result.html', {})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            return redirect('result.html')
