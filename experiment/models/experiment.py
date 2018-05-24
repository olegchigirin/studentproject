from django.db import models
from django.contrib.auth.models import User
from .datasource import DataSource


class Experiment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    data_source = models.ForeignKey(DataSource, related_name='data_source', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
