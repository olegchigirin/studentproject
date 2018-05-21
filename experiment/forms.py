from django.forms import ModelForm
from .models import Experiment, DataSet, DataSource


class ExperimentForm(ModelForm):
    class Meta:
        model = Experiment
        fields = ['name', 'description']


class DataSourceForm(ModelForm):
    class Meta:
        model = DataSource
        fields = ['name', 'source', 'description', 'experiment']


class DataSetForm(ModelForm):
    class Meta:
        model = DataSet
        fields = ['name', 'column_dtypes', 'column_dtypes', 'description', 'data_source', 'data_file']
