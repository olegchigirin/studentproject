from django.db import models

from experiment.models import Experiment


class DataSet(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name='experiment')
    data_file = models.FileField(upload_to='data-set/%Y/%m/%d')
