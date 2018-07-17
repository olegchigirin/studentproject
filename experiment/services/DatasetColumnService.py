from typing import List

from experiment.models import DatasetColumn, Dataset


def load_dataset_columns_by_dataset_name(name: str) -> List[DatasetColumn]:
    return DatasetColumn.objects.filter(dataset__name=name)
