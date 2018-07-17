from typing import List, Dict

import pandas as pd
import os
import kaggle
import chardet
import csv
from datetime import datetime
from urllib import parse
from experiment.models import DatasetColumn, Dataset, Experiment
from experiment.forms import DatasetKaggleURLForm, DatasetKaggleCreateForm, DatasetLocalCreateForm, \
    DatasetKaggleFileForm
from experiment.services import ExperimentService
from studentproject.settings import MEDIA_ROOT
import zipfile


def load_dataset_by_experiment_name(experiment: str) -> List[Dataset]:
    dataset_queryset = Dataset.objects.filter(experiment__name=experiment)
    return dataset_queryset


def create_columns(dataset: Dataset):
    file = dataset.data_file.path
    detector = chardet.UniversalDetector()
    detector.reset()
    with open(file, 'r', encoding='utf=8') as f:
        df = pd.read_csv(file, error_bad_lines=False, nrows=2)
        names = df.columns.values.tolist()
        dtypes = df.dtypes.tolist()
        for name, dtype in zip(names, dtypes):
            DatasetColumn.objects.create(label=name, datatype=dtype, dataset=dataset)


def get_kaggle_file_list(form: DatasetKaggleURLForm) -> Dict:
    kaggle_url = form.cleaned_data['kaggle_url']
    kaggle_url = parse.urlparse(kaggle_url).path[1:]
    files = kaggle.api.dataset_list_files(dataset=kaggle_url)
    return {'kaggle_url': kaggle_url,
            'files': files}


def download_kaggle_files(form: DatasetKaggleURLForm):
    kaggle_url = form.cleaned_data['kaggle_url']
    kaggle_url = parse.urlparse(kaggle_url).path[1:]
    path = os.path.join(MEDIA_ROOT, 'data-set/kaggle/%s' % kaggle_url)
    files = kaggle.api.dataset_list_files(dataset=kaggle_url)
    for file in files.files:
        if str(file).endswith('.csv'):
            kaggle.api.dataset_download_file(dataset=kaggle_url, file_name=str(file), path=path, force=True)
    for file in os.listdir(path):
        if file.endswith('.zip'):
            file_path = os.path.join(path, file)
            zip_ref = zipfile.ZipFile(file_path)
            zip_ref.extractall(path=path)
            zip_ref.close()
            os.remove(file_path)
    return path


def create_kaggle_datasets(path: str, experiment: str):
    for file in os.listdir(path):
        if file.endswith('.csv'):
            dataset = DatasetKaggleCreateForm()
            dataset = dataset.save(commit=False)
            dataset.experiment = ExperimentService.load_experiment_by_name(name=experiment)
            dataset.data_file = os.path.join(path, file)
            dataset.label = os.path.basename(file)
            dataset.save()
            create_columns(dataset=dataset)


def create_local_dataset(form: DatasetLocalCreateForm, experiment_name: str) -> Dataset:
    dataset: Dataset = form.save(commit=False)
    dataset.experiment = ExperimentService.load_experiment_by_name(experiment_name)
    return dataset
