from django.urls import path

import experiment.views
import experiment.views.main_views

app_name = 'experiment'

urlpatterns = [
    path('signup', experiment.views.user_views.SignUpView.as_view(), name='signup'),
    path('', experiment.views.main_views.home, name='home'),
    path('all', experiment.views.experiment_views.AllExperimentsView.as_view(), name='experiment_all'),
    path('<int:experiment>/', experiment.views.experiment_views.ExperimentDetailView.as_view(),
         name='experiment_details'),
    path('create', experiment.views.experiment_views.ExperimentCreateView.as_view(), name='experiment_create'),
    path('<int:experiment>/dataset/create', experiment.views.dataset_views.DataSetCreateView.as_view(),
         name='dataset_create'),
    path('<int:experiment>/dataset/', experiment.views.dataset_views.DataSetListView.as_view(),
         name='dataset_list'),
    path('<int:experiment>/dataset/<int:dataset>/', experiment.views.dataset_views.DataSetDetailView.as_view(),
         name='dataset_details'),
    path('<int:experiment>/dataset/<int:dataset>/column/<int:column>',
         experiment.views.dataset_columns_view.DataSetColumnUpdateView.as_view(), name='column_update'),
    path('<int:experiment>/update', experiment.views.experiment_views.ExperimentUpdateView.as_view(),
         name='experiment_update')
]
