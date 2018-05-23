from django.urls import reverse
from django.views import generic

from experiment.forms import DataSetCreateForm
from experiment.models import DataSet, DataSource, DataSetColumns
from experiment.services import create_column_object


class DataSetCreateView(generic.CreateView):
    model = DataSet
    template_name = 'experiment/dataset/dataset_create.html'
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
    template_name = 'experiment/dataset/dataset_list.html'
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
    template_name = 'experiment/dataset/dataset_detail.html'
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