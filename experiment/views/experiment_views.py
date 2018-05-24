from django.urls import reverse
from django.views import generic
from django.contrib.auth import mixins

from experiment.forms import ExperimentCreateForm
from experiment.models import Experiment


class AllExperimentsView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = 'experiment/experiment/experiment_list.html'
    context_object_name = 'experiment_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AllExperimentsView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_queryset(self):
        return Experiment.objects.filter(user=self.request.user)


class ExperimentCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Experiment
    form_class = ExperimentCreateForm
    template_name = 'experiment/experiment/experiment_create.html'

    def form_valid(self, form: ExperimentCreateForm):
        experiment: Experiment = form.save(commit=False)
        experiment.user = self.request.user
        experiment.save()
        return super(ExperimentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('experiment:experiment_details', kwargs={'experiment': self.object.pk})


class ExperimentDetailView(generic.DetailView):
    model = Experiment
    template_name = 'experiment/experiment/experiment_details.html'
    context_object_name = 'experiment_details'
    pk_url_kwarg = 'experiment'

    def get_context_data(self, **kwargs):
        context = super(ExperimentDetailView, self).get_context_data(**kwargs)
        context['experiment']: int = self.kwargs.get('experiment')
        context['user'] = self.request.user
        return context


class ExperimentUpdateView(generic.UpdateView):
    model = Experiment
    form_class = ExperimentCreateForm
    template_name = 'experiment/experiment/experiment_update.html'
    pk_url_kwarg = 'experiment'

    def get_context_data(self, **kwargs):
        context = super(ExperimentUpdateView, self).get_context_data(**kwargs)
        context['experiment'] = self.kwargs.get('experiment')
        return context

    def get_success_url(self):
        return reverse('experiment:experiment_detail', kwargs={'experiment': self.kwargs.get('experiment')})
