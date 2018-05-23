from django.db import models

from experiment.models import Experiment


class DataSource(models.Model):
    name = models.CharField(max_length=200)
    source = models.CharField(max_length=200, default='Personal data')
    description = models.TextField(max_length=2000)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name='experiment')
