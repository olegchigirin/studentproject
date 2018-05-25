import pandas as pd
import os
import kaggle
import chardet
import csv
from datetime import datetime
from urllib import parse
from .models import DataSetColumn, DataSet, Experiment
from .forms import DataSetKaggleURLForm, DataSetKaggleCreateForm
from studentproject.settings import MEDIA_ROOT
import zipfile


def create_column_object(dataset_pk: int):
    dataset = DataSet.objects.get(pk=dataset_pk)
    file = dataset.data_file.path
    data = open(file, 'rb').read()
    encoding = chardet.detect(data)['encoding']
    try:
        df = pd.read_csv(file, error_bad_lines=False, nrows=2)
    except UnicodeDecodeError:
        df = pd.read_csv(file, error_bad_lines=False, nrows=2, encoding=encoding)
    names = df.columns.values.tolist()
    dtypes = df.dtypes.tolist()
    for name, dtype in zip(names, dtypes):
        DataSetColumn.objects.create(column_name=name, column_dtype=dtype, dataset=dataset)


def download_kaggle_files(form: DataSetKaggleURLForm):
    kaggle_url = form.cleaned_data['kaggle_url']
    kaggle_url = parse.urlparse(kaggle_url).path[1:]
    path = os.path.join(MEDIA_ROOT, 'data-set/kaggle/%s' % kaggle_url)
    files = kaggle.api.dataset_list_files(dataset=kaggle_url)
    for file in files.files:
        if str(file).endswith('.csv'):
            kaggle.api.dataset_download_file(dataset=kaggle_url, file=str(file), path=path, force=True)
    for file in os.listdir(path):
        if file.endswith('.zip'):
            file_path = os.path.join(path, file)
            zip_ref = zipfile.ZipFile(file_path)
            zip_ref.extractall(path=path)
            zip_ref.close()
            os.remove(file_path)
    return path


def create_kaggle_datasets(path: str, experiment: int):
    for file in os.listdir(path):
        if file.endswith('.csv'):
            dataset = DataSetKaggleCreateForm()
            dataset = dataset.save(commit=False)
            dataset.experiment = Experiment.objects.get(pk=experiment)
            dataset.data_file = os.path.join(path, file)
            dataset.name = os.path.basename(file)
            dataset.save()
            create_column_object(dataset.pk)
