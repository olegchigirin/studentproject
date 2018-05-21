from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import Experiment, DataSource, DataSet


# Create your views here.

def index(request):
    return render(request, 'experiment/experiment_home.html')


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


class DataSourceCreateView(generic.CreateView):
    model = DataSource
    template_name = 'experiment/data_source_create.html'
    fields = ['name', 'source', 'description', 'experiment']

    def get_initial(self):
        return {
            'experiment': Experiment.objects.get(id=self.kwargs.get('pk'))
        }

    def get_success_url(self):
        return reverse('experiment:experiment_detail', kwargs={'pk': self.kwargs.get('pk')})


class DataSourceListView(generic.ListView):
    template_name = 'experiment/data_source_list.html'
    context_object_name = 'data_source_list'

    def get_queryset(self):
        return DataSource.objects.filter(experiment=self.kwargs.get('pk'))


class DataSourceDetailView(generic.DetailView):
    model = DataSource
    template_name = 'experiment/data_source_details.html'
    context_object_name = 'data_source_details'


class DataSetCreateView(generic.CreateView):
    model = DataSet
    template_name = 'experiment/dataset_create.html'
    fields = ['name', 'column_names', 'column_dtypes', 'description', 'data_source', 'data_file']

    def get_initial(self):
        return {
            'data_source': DataSource.objects.get(id=self.kwargs.get('source'))
        }

    def get_success_url(self):
        return reverse('experiment:data_source_details', kwargs={'experiment': self.kwargs.get('experiment'),
                                                                 'pk': self.kwargs.get('source')})


class DataSetListView(generic.ListView):
    template_name = 'experiment/dataset_list.html'
    context_object_name = 'dataset_list'

    def get_queryset(self):
        return DataSet.objects.filter(data_source=self.kwargs.get('source'))
