from django.db import models
from .Common import Auditable


class DataSource(Auditable):
    LOCAL = 'local'
    KAGGLE = 'kaggle'

    DATA_SOURCE_TYPES = (
        (LOCAL, 'local'),
        (KAGGLE, 'kaggle')
    )

    source = models.CharField(verbose_name='Data Source', max_length=20, choices=DATA_SOURCE_TYPES, unique=True)
    description = models.TextField(verbose_name='Description', max_length=2000)

    class Meta:
        verbose_name = 'Data Source'
        verbose_name_plural = "Data Sources"

    def __str__(self):
        return self.source

    def data_source_name(self):
        return self.name

    def data_source_update_date(self):
        return self.updated_at
