from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from experiment.forms import ExperimentCreateForm, DataSourceCreateForm, DataSetCreateForm
from .models import Experiment, DataSource, DataSet, DataSetColumns
from .services import create_column_object


# Create your views here.

def home(request):
    return render(request, 'experiment/experiment_home.html')


class AllExperimentsView(generic.ListView):
    template_name = 'experiment/experiment_list.html'
    context_object_name = 'all_experiments_list'

    def get_queryset(self):
        return Experiment.objects.all()


class ExperimentCreateView(generic.CreateView):
    model = Experiment
    form_class = ExperimentCreateForm
    template_name = 'experiment/experiment_create.html'

    def get_success_url(self):
        return reverse('experiment:experiment_detail', kwargs={'pk': self.object.pk})


class ExperimentDetailView(generic.DetailView):
    model = Experiment
    template_name = 'experiment/experiment_details.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        experiment_id = self.kwargs.get('pk')
        context = {
            'experiment_details': self.get_object(),
            'experiment_id': experiment_id
        }
        return context


class DataSourceCreateView(generic.CreateView):
    model = DataSource
    form_class = DataSourceCreateForm
    template_name = 'experiment/data_source_create.html'

    def get_initial(self):
        return {'experiment': Experiment.objects.get(id=self.kwargs.get('pk'))}

    def form_valid(self, form: DataSourceCreateForm):
        data_source: DataSource = form.save(commit=False)
        data_source.experiment = self.get_initial()['experiment']
        data_source.save()
        return super(DataSourceCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('experiment:data_source_details', kwargs={'experiment': self.kwargs.get('pk'),
                                                                 'pk': self.object.pk})


class DataSourceListView(generic.ListView):
    template_name = 'experiment/data_source_list.html'
    context_object_name = 'data_source_list'

    def get_queryset(self):
        return DataSource.objects.filter(experiment=self.kwargs.get('pk'))

    def get_context_data(self, *, object_list=None, **kwargs):
        experiment = self.kwargs.get('pk')
        context = {
            'data_source_list': self.get_queryset(),
            'experiment': experiment
        }
        context.update(kwargs)
        return context


class DataSourceDetailView(generic.DetailView):
    model = DataSource
    template_name = 'experiment/data_source_details.html'
    context_object_name = 'data_source_details'

    def get_context_data(self, **kwargs):
        data_source = DataSource.objects.get(pk=self.kwargs.get('pk'))
        context = {
            'data_source': data_source,
            'experiment': self.kwargs.get('experiment'),
            'source': self.kwargs.get('pk')
        }
        return context


class DataSetCreateView(generic.CreateView):
    model = DataSet
    template_name = 'experiment/dataset_create.html'
    form_class = DataSetCreateForm

    def get_initial(self):
        return {
            'data_source': DataSource.objects.get(id=self.kwargs.get('source'))
        }

    def get_success_url(self):
        return reverse('experiment:dataset_details', kwargs={'experiment': self.kwargs.get('experiment'),
                                                             'source': self.kwargs.get('source'),
                                                             'pk': self.object.pk})

    def form_valid(self, form):
        dataset: DataSet = form.save(commit=False)
        dataset.data_source = self.get_initial()['data_source']
        dataset.save()
        create_column_object(dataset.pk)
        return super(DataSetCreateView, self).form_valid(form)


class DataSetListView(generic.ListView):
    template_name = 'experiment/dataset_list.html'
    context_object_name = 'dataset_list'

    def get_queryset(self):
        return DataSet.objects.filter(data_source=self.kwargs.get('source'))

    def get_context_data(self, *, object_list=None, **kwargs):
        experiment = self.kwargs.get('experiment')
        source = self.kwargs.get('source')
        context = {
            'dataset_list': self.get_queryset(),
            'experiment': experiment,
            'source': source
        }
        context.update(kwargs)
        return context


class DataSetDetailView(generic.DetailView):
    model = DataSet
    template_name = 'experiment/dataset_detail.html'
    context_object_name = 'context'

    def get_context_data(self, **kwargs):
        dataset = DataSet.objects.get(pk=self.kwargs.get('pk'))
        dataset_columns = DataSetColumns.objects.filter(dataset=dataset)
        context = {
            'dataset_detail': dataset,
            'dataset_columns': dataset_columns,
            'experiment': self.kwargs.get('experiment'),
            'source': self.kwargs.get('source')
        }
        return context
