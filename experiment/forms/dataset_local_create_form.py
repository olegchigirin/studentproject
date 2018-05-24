from django import forms

from experiment.models import DataSet


class DataSetLocalCreateForm(forms.ModelForm):
    class Meta:
        model = DataSet
        exclude = ['experiment']
