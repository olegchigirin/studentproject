from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage(location='filestorage')


class Experiment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
