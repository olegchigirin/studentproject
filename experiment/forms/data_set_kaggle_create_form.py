from django import forms

from experiment.models import DataSet


class DataSetKaggleCreateForm(forms.ModelForm):
    class Meta:
        model = DataSet
        exclude = ['experiment', 'data_file', 'description', 'name']
