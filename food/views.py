from django.shortcuts import render, redirect
from .forms import UploadFileForm

# Create your views here.
def home(request):
    return render(request, 'food/food.html', {})

def result(request):
    return render(request, 'food/result.html', {})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            return redirect('food/result.html')
