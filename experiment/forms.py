from django import forms
import pandas as pd
from .models import Experiment, DataSet, DataSource, DataSetColumns


class ExperimentCreateForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['name', 'description']


class DataSourceCreateForm(forms.ModelForm):
    class Meta:
        model = DataSource
        exclude = ['experiment']


class DataSetCreateForm(forms.ModelForm):
    class Meta:
        model = DataSet
        exclude = ['data_source']



