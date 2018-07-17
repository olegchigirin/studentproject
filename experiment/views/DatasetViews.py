from typing import List

from django.urls import reverse
from django.views import generic
from django.contrib.auth import mixins

from experiment.forms import DatasetLocalCreateForm, DatasetKaggleCreateForm, DatasetKaggleURLForm, \
    DatasetKaggleFileForm
from experiment.models import Dataset, Experiment, DatasetColumn, DataSource
from experiment.services import DatasetService, ExperimentService, DatasetColumnService


class DatasetListView(mixins.LoginRequiredMixin, generic.ListView):
    template_name = 'experiment/dataset/dataset_list.html'
    context_object_name = 'context'

    def get_queryset(self):
        return DatasetService.load_dataset_by_experiment_name(self.kwargs['experiment'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DatasetListView, self).get_context_data(**kwargs)
        experiment = self.kwargs['experiment']
        dataset_list = self.get_queryset()
        context['dataset_list'] = dataset_list
        context['experiment'] = experiment
        return context


class DatasetCreateView(mixins.LoginRequiredMixin, generic.FormView):
    model = Dataset
    template_name = 'experiment/dataset/dataset_create.html'
    object_created = False
    files = None
    kaggle_url = None

    def get_context_data(self, **kwargs):
        context = super(DatasetCreateView, self).get_context_data(**kwargs)
        context['experiment'] = self.kwargs.get('experiment')
        return context

    def get_form_class(self):
        experiment = ExperimentService.load_experiment_by_name(name=self.kwargs['experiment'])
        source = experiment.source.source
        if source == DataSource.LOCAL:
            return DatasetLocalCreateForm
        if source == DataSource.KAGGLE:
            return DatasetKaggleURLForm

    def get_success_url(self):
        experiment = ExperimentService.load_experiment_by_name(name=self.kwargs['experiment'])
        source = experiment.source.source
        if source == DataSource.LOCAL:
            return reverse('experiment:dataset_list', kwargs={'experiment': self.kwargs.get('experiment')})
        if source == DataSource.KAGGLE:  # TODO: Fix this
            kwargs = self.files
            return reverse('experiment:dataset_file_list', kwargs={'experiment': self.kwargs['experiment'],
                                                                   'files': kwargs['files'],
                                                                   'kaggle_url': kwargs['kaggle_url']})

    def form_valid(self, form):
        if isinstance(form, DatasetLocalCreateForm):
            dataset = DatasetService.create_local_dataset(form=form, experiment_name=self.kwargs['experiment'])
            dataset.save()
            DatasetService.create_columns(dataset)
            return super(DatasetCreateView, self).form_valid(form)
        if isinstance(form, DatasetKaggleURLForm):
            self.files = DatasetService.get_kaggle_file_list(form)
            return super(DatasetCreateView, self).form_valid(form)


class DatasetKaggleFilesViews(mixins.LoginRequiredMixin, generic.FormView):
    model = Dataset
    template_name = 'experiment/dataset/dataset_file_list.html'
    context_object_name = 'dataset_files'

    def get_context_data(self, **kwargs):
        context = super(DatasetKaggleFilesViews, self).get_context_data(**kwargs)
        context['experiment'] = self.kwargs['experiment']
        context['files'] = self.kwargs['files']
        return context

    def get_form_class(self):
        kwargs = {
            'kaggle_url': self.kwargs['kaggle_url'],
            'files': self.kwargs['files']
        }
        return DatasetKaggleFileForm(kwargs)

    def get_success_url(self):
        return reverse('experiment:home')


class DatasetDetailView(mixins.LoginRequiredMixin, generic.DetailView):
    model = Dataset
    template_name = 'experiment/dataset/dataset_details.html'
    context_object_name = 'dataset_details'
    slug_field = 'name'
    slug_url_kwarg = 'dataset'

    def get_context_data(self, **kwargs):
        context = super(DatasetDetailView, self).get_context_data(**kwargs)
        context['experiment'] = self.kwargs['experiment']
        context['dataset_columns']: List[DatasetColumn] = DatasetColumnService. \
            load_dataset_columns_by_dataset_name(self.kwargs['dataset'])
        return context
