from django.urls import reverse
from django.views import generic

from experiment.forms import ExperimentCreateForm
from experiment.models import Experiment


class AllExperimentsView(generic.ListView):
    template_name = 'experiment/experiment/experiment_list.html'
    context_object_name = 'all_experiments_list'

    def get_queryset(self):
        return Experiment.objects.all()


class ExperimentCreateView(generic.CreateView):
    model = Experiment
    form_class = ExperimentCreateForm
    template_name = 'experiment/experiment/experiment_create.html'

    def get_success_url(self):
        return reverse('experiment:experiment_detail', kwargs={'pk': self.object.pk})


class ExperimentDetailView(generic.DetailView):
    model = Experiment
    template_name = 'experiment/experiment/experiment_details.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        experiment_id = self.kwargs.get('pk')
        context = {
            'experiment_details': self.get_object(),
            'experiment_id': experiment_id
        }
        return context