from django.contrib import admin

from .models import Experiment, DataSet, DataSource, DataSetColumn

# Register your models here.

admin.site.register(Experiment)
admin.site.register(DataSet)
admin.site.register(DataSource)
admin.site.register(DataSetColumn)
