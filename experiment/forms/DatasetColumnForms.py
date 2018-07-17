from django import forms

from experiment.models import DatasetColumn


class DataSetColumnUpdateForm(forms.ModelForm):
    class Meta:
        model = DatasetColumn
        fields = ['label', 'description']