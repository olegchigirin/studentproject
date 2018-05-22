from django.db import models


# Create your models here.

class Experiment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)


class DataSource(models.Model):
    name = models.CharField(max_length=200)
    source = models.CharField(max_length=200, default='Personal data')
    description = models.TextField(max_length=2000)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, related_name='experiment')


class DataSet(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE, related_name='data_source')
    data_file = models.FileField(upload_to='data-set/%Y/%m/%d')


class DataSetColumns(models.Model):
    column_name = models.CharField(max_length=200, unique=False)
    column_dtype = models.CharField(max_length=100)
    column_description = models.CharField(max_length=2000, null=True)
    dataset = models.ForeignKey(DataSet, on_delete=models.CASCADE, related_name='dataset')


