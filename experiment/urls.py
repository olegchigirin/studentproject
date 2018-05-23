from django.urls import path
import experiment.views
import experiment.views.dataset_views
import experiment.views.datasource_views
import experiment.views.experiment_views
import experiment.views.main_views
from . import views

app_name = 'experiment'

urlpatterns = [
    path('', experiment.views.main_views.home, name='home'),
    path('all', experiment.views.experiment_views.AllExperimentsView.as_view(), name='all_experiments'),
    path('<int:pk>/', experiment.views.experiment_views.ExperimentDetailView.as_view(), name='experiment_detail'),
    path('create', experiment.views.experiment_views.ExperimentCreateView.as_view(), name='experiment__create'),
    path('<int:pk>/data-source/create', experiment.views.datasource_views.DataSourceCreateView.as_view(),
         name='data_source_create'),
    path('<int:pk>/data-source/', experiment.views.datasource_views.DataSourceListView.as_view(),
         name='data_source_list'),
    path('<int:experiment>/data-source/<int:pk>', experiment.views.datasource_views.DataSourceDetailView.as_view(),
         name='data_source_details'),
    path('<int:experiment>/data-source/<int:source>/dataset/create',
         experiment.views.dataset_views.DataSetCreateView.as_view(),
         name='data_set_create'),
    path('<int:experiment>/data-source/<int:source>/dataset/', experiment.views.dataset_views.DataSetListView.as_view(),
         name='dataset_list'),
    path('<int:experiment>/data-source/<int:source>/dataset/<int:pk>/',
         experiment.views.dataset_views.DataSetDetailView.as_view(),
         name='dataset_details')
]
