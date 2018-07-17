from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.contrib.auth import mixins

from experiment.forms import ExperimentCreateForm
from experiment.models import Experiment
from experiment.services import ExperimentService


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
        ExperimentService.save_experiment(form=form, user=self.request.user)
        return super(ExperimentCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('experiment:experiment_details', kwargs={'experiment': self.object.name})


class ExperimentDetailView(mixins.LoginRequiredMixin, generic.DetailView):
    model = Experiment
    template_name = 'experiment/experiment/experiment_details.html'
    context_object_name = 'experiment_details'
    slug_field = 'name'
    slug_url_kwarg = 'experiment'

    def get_context_data(self, **kwargs):
        context = super(ExperimentDetailView, self).get_context_data(**kwargs)
        context['experiment']: str = self.kwargs.get('experiment')
        context['user']: User = self.request.user
        return context


class ExperimentUpdateView(mixins.LoginRequiredMixin, generic.UpdateView):
    model = Experiment
    form_class = ExperimentCreateForm
    template_name = 'experiment/experiment/experiment_update.html'
    slug_field = 'name'
    slug_url_kwarg = 'experiment'

    def get_context_data(self, **kwargs):
        context = super(ExperimentUpdateView, self).get_context_data(**kwargs)
        context['experiment'] = self.kwargs.get('experiment')
        return context

    def get_success_url(self):
        return reverse('experiment:experiment_detail', kwargs={'experiment': self.kwargs.get('experiment')})
