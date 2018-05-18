from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Experiment


# Create your views here.

def index(request):
    return render(request, 'experiment/experiment_index.html')


class AllExperimentsView(generic.ListView):
    template_name = 'experiment/experiment_list.html'
    context_object_name = 'all_experiments_list'

    def get_queryset(self):
        return Experiment.objects.all()


class ExperimentDetailView(generic.DetailView):
    model = Experiment
    template_name = 'experiment/experiment_details.html'
    context_object_name = 'experiment_details'


class ExperimentCreateView(generic.CreateView):
    model = Experiment
    fields = ['name', 'description']
    template_name = 'experiment/experiment_create.html'

    def get_success_url(self):
        return reverse('experiment:experiment_detail', kwargs={'pk': self.object.pk})
