from django.db import models
from experiment.models import Dataset
from .Common import Auditable


class DatasetColumn(Auditable):
    OBJECT = 'object'
    INT64 = 'int64'
    FLOAT64 = 'float'
    BOOL = 'bool'
    DATETIME64 = 'datetime64'
    TIMEDELTA = 'timedelta[ns]'
    CATEGORY = 'category'

    COLUMN_DATATYPES = (
        (OBJECT, 'object'),
        (INT64, 'int64'),
        (FLOAT64, 'float64'),
        (BOOL, 'bool'),
        (DATETIME64, 'datetime64'),
        (TIMEDELTA, 'timedelta[ns]'),
        (CATEGORY, 'category')
    )

    class Meta:
        verbose_name = 'Dataset Column'
        verbose_name_plural = 'Dataset Columns'
        ordering = ['label']

    label = models.CharField(verbose_name='Column name', max_length=200, unique=False)
    datatype = models.CharField(verbose_name='Column datatype', max_length=50, choices=COLUMN_DATATYPES)
    description = models.CharField(verbose_name='Column description', max_length=2000, null=True)
    dataset = models.ForeignKey(Dataset, verbose_name='Column in dataset', on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.label, self.datatype)
