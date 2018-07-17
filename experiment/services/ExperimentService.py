from django.contrib.auth.models import User

from experiment.models import Experiment
from experiment.forms.ExperimentForms import ExperimentCreateForm


def save_experiment(form: ExperimentCreateForm, user: User):
    experiment: Experiment = form.save(commit=False)
    experiment.user = user
    experiment.save()


def load_experiment_by_name(name: str) -> Experiment:
    return Experiment.objects.get(name=name)
