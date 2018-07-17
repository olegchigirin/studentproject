from django.urls import reverse
from django.views import generic
from django.contrib.auth import mixins

from experiment.forms import DataSetColumnUpdateForm
from experiment.models import DatasetColumn


class DataSetColumnUpdateView(mixins.LoginRequiredMixin, generic.UpdateView):
    model = DatasetColumn
    form_class = DataSetColumnUpdateForm
    template_name = 'experiment/dataset/dataset_columns/dataset_column_update.html'
    slug_field = 'name'
    slug_url_kwarg = 'column'

    def get_success_url(self):
        return reverse('experiment:dataset_details', kwargs={'experiment': self.kwargs.get('experiment'),
                                                             'dataset': self.kwargs.get('dataset')})
