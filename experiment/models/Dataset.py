from django.db import models

from experiment.models import Experiment
from experiment.models.Common import Auditable


class Dataset(Auditable):
    class Meta:
        verbose_name = 'dataset'
        verbose_name_plural = 'datasets'

    label = models.CharField(verbose_name='Label', max_length=200)
    description = models.CharField(verbose_name='Description', max_length=2000, null=True)
    experiment = models.ForeignKey(Experiment, verbose_name='Dataset in experiment', on_delete=models.CASCADE)
    data_file = models.FileField(verbose_name='Data file', max_length=500, upload_to='data-set/local/%Y/%m/%d',
                                 null=True)

    def __str__(self):
        return self.label
