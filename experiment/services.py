import pandas as pd
from .models import DataSetColumn, DataSet


def create_column_object(dataset_pk: int):
    dataset = DataSet.objects.get(pk=dataset_pk)
    df = pd.read_csv(dataset.data_file, error_bad_lines=False)
    names = df.columns.values.tolist()
    dtypes = df.dtypes.tolist()
    for name, dtype in zip(names, dtypes):
        DataSetColumn.objects.create(column_name=name, column_dtype=dtype, dataset=dataset)
