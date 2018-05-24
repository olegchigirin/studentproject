from django.db import models
from experiment.utils import ChoiceEnum
from experiment.models import DataSet


class DataSetColumn(models.Model):
    class DataTypes(ChoiceEnum):
        OBJECT = 'object'
        INT64 = 'int64'
        FLOAT64 = 'float'
        BOOL = 'bool'
        DATETIME64 = 'datetime64'
        TIMEDELTA = 'timedelta[ns]'
        CATEGORY = 'category'

    column_name = models.CharField(max_length=200, unique=False)
    column_dtype = models.CharField(max_length=100, choices=DataTypes.choices())
    column_description = models.CharField(max_length=2000, null=True)
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE, related_name='dataset')
