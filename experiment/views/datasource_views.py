from django.urls import reverse
from django.views import generic

from experiment.forms import DataSourceCreateForm
from experiment.models import DataSource, Experiment


class DataSourceCreateView(generic.CreateView):
    model = DataSource
    form_class = DataSourceCreateForm
    template_name = 'experiment/datasource/data_source_create.html'

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
    template_name = 'experiment/datasource/data_source_list.html'
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
    template_name = 'experiment/datasource/data_source_details.html'
    context_object_name = 'data_source_details'

    def get_context_data(self, **kwargs):
        data_source = DataSource.objects.get(pk=self.kwargs.get('pk'))
        context = {
            'data_source': data_source,
            'experiment': self.kwargs.get('experiment'),
            'source': self.kwargs.get('pk')
        }
        return context