from django.urls import reverse
from django.views import generic

from experiment.forms import DataSetColumnUpdateForm
from experiment.models import DataSetColumn


class DataSetColumnUpdateView(generic.UpdateView):
    model = DataSetColumn
    form_class = DataSetColumnUpdateForm
    template_name = 'experiment/dataset/dataset_columns/dataset_column_update.html'
    pk_url_kwarg = 'column'

    def get_success_url(self):
        return reverse('experiment:dataset_details', kwargs={'experiment': self.kwargs.get('experiment'),
                                                             'dataset': self.kwargs.get('dataset')})
