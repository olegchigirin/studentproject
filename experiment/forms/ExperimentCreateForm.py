from django import forms

from experiment.models import Experiment


class ExperimentCreateForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['name', 'description']