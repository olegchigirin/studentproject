import pandas as pd
from .models import DataSetColumns, DataSet


def create_column_object(dataset_pk: int):
    dataset = DataSet.objects.get(pk=dataset_pk)
    df = pd.read_csv(dataset.data_file, error_bad_lines=False)
    names = df.columns.values.tolist()
    dtypes = df.dtypes.tolist()
    for name, dtype in zip(names, dtypes):
        DataSetColumns.objects.create(column_name=name, column_dtype=dtype, dataset=dataset)
