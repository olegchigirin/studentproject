from django.db import models

from experiment.models import DataSet


class DataSetColumn(models.Model):
    column_name = models.CharField(max_length=200, unique=False)
    column_dtype = models.CharField(max_length=100)
    column_description = models.CharField(max_length=2000, null=True)
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE, related_name='dataset')
