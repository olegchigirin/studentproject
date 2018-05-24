from django.db import models


class DataSource(models.Model):
    LOCAL = 'local'
    KAGGLE = 'kaggle'

    DATA_SOURCE_CHOICES = (
        (LOCAL, 'local'),
        (KAGGLE, 'kaggle')
    )

    source = models.CharField(max_length=20, choices=DATA_SOURCE_CHOICES, unique=True)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return self.source
