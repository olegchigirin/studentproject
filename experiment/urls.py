from django.urls import path, reverse

from . import views

app_name = 'experiment'

urlpatterns = [
    path('', views.index,name='index'),
    path('all', views.AllExperimentsView.as_view(), name='all_experiments'),
    path('<int:pk>/', views.ExperimentDetailView.as_view(), name='experiment_detail'),
    path('create', views.ExperimentCreateView.as_view(), name='experiment__create'),
]
