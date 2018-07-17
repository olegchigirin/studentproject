import uuid

from django.contrib.auth.models import User
from django.db import models

from experiment.utils import get_slug


class Identifiable(models.Model):
    id = models.UUIDField(verbose_name='id', primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True


class Auditable(Identifiable):
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Date of update', auto_now=True)
    name = models.SlugField(verbose_name='Name', unique=True, editable=False)

    class Meta:
        abstract = True
        ordering = ['-updated_by']

    def save(self, *args, **kwargs):
        if not self.name:
            model_name = self.__class__.__name__
            slug = get_slug(model_name)
            self.name = slug
        super().save(*args, **kwargs)
