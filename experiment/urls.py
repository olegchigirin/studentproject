from django.urls import path, reverse

from . import views

app_name = 'experiment'

urlpatterns = [
    path('', views.index, name='home'),
    path('all', views.AllExperimentsView.as_view(), name='all_experiments'),
    path('<int:pk>/', views.ExperimentDetailView.as_view(), name='experiment_detail'),
    path('create', views.ExperimentCreateView.as_view(), name='experiment__create'),
    path('<int:pk>/data-source/create', views.DataSourceCreateView.as_view(), name='data_source_create'),
    path('<int:pk>/data-source/', views.DataSourceListView.as_view(), name='data_source_list'),
    path('<int:experiment>/data-source/<int:pk>', views.DataSourceDetailView.as_view(), name='data_source_details'),
    path('<int:experiment>/data-source/<int:source>/dataset/create', views.DataSetCreateView.as_view(),
         name='data_set_create'),
    path('<int:experiment>/data-source/<int:source>/dataset/', views.DataSetListView.as_view(), name='dataset_list')
]
