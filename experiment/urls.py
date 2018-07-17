from django.urls import path

import experiment.views
import experiment.views.MainViews

app_name = 'experiment'

urlpatterns = [
    path('signup', experiment.views.UserViews.SignUpView.as_view(), name='signup'),
    path('', experiment.views.MainViews.home, name='home'),
    path('all', experiment.views.ExperimentViews.AllExperimentsView.as_view(), name='experiment_all'),
    path('<str:experiment>/', experiment.views.ExperimentViews.ExperimentDetailView.as_view(),
         name='experiment_details'),
    path('create', experiment.views.ExperimentViews.ExperimentCreateView.as_view(), name='experiment_create'),
    path('<str:experiment>/dataset/create', experiment.views.DatasetViews.DatasetCreateView.as_view(),
         name='dataset_create'),
    path('<str: experiment>/dataset/file-list', experiment.views.DatasetViews.DatasetKaggleFilesViews.as_view(),
         name='dataset_file_list'),
    path('<str:experiment>/dataset/', experiment.views.DatasetViews.DatasetListView.as_view(),
         name='dataset_list'),
    path('<str:experiment>/dataset/<str:dataset>/', experiment.views.DatasetViews.DatasetDetailView.as_view(),
         name='dataset_details'),
    path('<str:experiment>/dataset/<str:dataset>/column/<str:column>',
         experiment.views.DatasetColumnViews.DataSetColumnUpdateView.as_view(), name='column_update'),
    path('<str:experiment>/update', experiment.views.ExperimentViews.ExperimentUpdateView.as_view(),
         name='experiment_update'),
]
