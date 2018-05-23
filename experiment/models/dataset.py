from django.db import models

from experiment.models import DataSource


class DataSet(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE, related_name='data_source')
    data_file = models.FileField(upload_to='data-set/%Y/%m/%d')
