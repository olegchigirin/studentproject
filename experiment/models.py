from django.db import models


# Create your models here.

class Experiment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)


class DataSource(models.Model):
    name = models.CharField(max_length=200)
    source = models.CharField(max_length=200, default='Personal data')
    description = models.TextField(max_length=2000)
    experiment = models.ForeignKey(Experiment, on_delete=models.SET_NULL, null=True)


class DataSet(models.Model):
    name = models.CharField(max_length=200)
    column_names = models.CharField(max_length=400)
    column_dtypes = models.CharField(max_length=400)
    description = models.TextField(max_length=2000)
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE, null=False)
    data_file = models.FileField(upload_to='data-set/%Y/%m/%d')
