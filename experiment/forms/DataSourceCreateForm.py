from django import forms

from experiment.models import DataSource


class DataSourceCreateForm(forms.ModelForm):
    class Meta:
        model = DataSource
        exclude = ['experiment']