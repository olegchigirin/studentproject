from django.db import models
from django.contrib.auth.models import User
from .DataSource import DataSource
from .Common import Auditable


class Experiment(Auditable):
    label = models.CharField(verbose_name='Label', max_length=200)
    description = models.TextField(verbose_name='Description', max_length=2000)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    source = models.ForeignKey(DataSource, verbose_name='Data Source', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Experiment'
        verbose_name_plural = 'Experiments'
        ordering = ['-updated_at', 'user']

    def __str__(self):
        return self.label
