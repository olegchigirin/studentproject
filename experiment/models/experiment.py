from django.db import models


class Experiment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)