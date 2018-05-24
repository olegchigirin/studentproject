from django import forms

from experiment.models import DataSetColumn


class DataSetColumnUpdateForm(forms.ModelForm):
    class Meta:
        model = DataSetColumn
        fields = ['column_name', 'column_description']
