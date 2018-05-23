from django import forms

from experiment.models import DataSet


class DataSetCreateForm(forms.ModelForm):
    class Meta:
        model = DataSet
        exclude = ['data_source']