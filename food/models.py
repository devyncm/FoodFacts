from django.db import models

# Create your models here.

class UploadedPhoto(models.Model):
    photo = models.ImageField(upload_to='photos/')