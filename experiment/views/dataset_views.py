from django.urls import reverse
from django.views import generic

from experiment.forms import DataSetLocalCreateForm, DataSetKaggleCreateForm
from experiment.models import DataSet, Experiment, DataSetColumn, DataSource
from experiment.services import create_column_object


class DataSetCreateView(generic.CreateView):
    model = DataSet
    template_name = 'experiment/dataset/dataset_create.html'

    def get_context_data(self, **kwargs):
        context = super(DataSetCreateView, self).get_context_data(**kwargs)
        context['experiment'] = self.kwargs.get('experiment')
        return context

    def get_form_class(self):
        experiment = Experiment.objects.get(pk=self.kwargs.get('experiment'))
        data_source = experiment.data_source
        source = data_source.source
        if source == DataSource.LOCAL:
            return DataSetLocalCreateForm
        if source == DataSource.KAGGLE:
            return DataSetKaggleCreateForm

    def get_success_url(self):
        return reverse('experiment:dataset_details', kwargs={'experiment': self.kwargs.get('experiment'),
                                                             'dataset': self.object.pk})

    def form_valid(self, form):
        dataset: DataSet = form.save(commit=False)
        dataset.experiment = Experiment.objects.get(pk=self.kwargs.get('experiment'))
        dataset.save()
        create_column_object(dataset.pk)
        return super(DataSetCreateView, self).form_valid(form)


class DataSetListView(generic.ListView):
    template_name = 'experiment/dataset/dataset_list.html'
    context_object_name = 'context'

    def get_queryset(self):
        return DataSet.objects.filter(experiment=self.kwargs.get('experiment'))

    def get_context_data(self, *, object_list=None, **kwargs):
        experiment = self.kwargs.get('experiment')
        context = {
            'dataset_list': self.get_queryset(),
            'experiment': experiment,
        }
        context.update(kwargs)
        return context


class DataSetDetailView(generic.DetailView):
    model = DataSet
    template_name = 'experiment/dataset/dataset_details.html'
    context_object_name = 'dataset_details'
    pk_url_kwarg = 'dataset'

    def get_context_data(self, **kwargs):
        context = super(DataSetDetailView, self).get_context_data(**kwargs)
        context['experiment'] = self.kwargs.get('experiment')
        context['source'] = self.kwargs.get('source')
        context['dataset_columns']: DataSetColumn = DataSetColumn.objects.filter(dataset=self.get_object())
        return context
