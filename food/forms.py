from django import forms
from .models import *

class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = UploadedPhoto
        fields = ['photo']