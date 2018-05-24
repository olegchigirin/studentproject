from django import forms

from experiment.models import DataSet


class DataSetKaggleCreateForm(forms.ModelForm):
    kaggle_url = forms.URLField()

    class Meta:
        model = DataSet
        exclude = ['experiment', 'data_file']
