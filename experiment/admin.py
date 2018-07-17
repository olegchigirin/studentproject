from django.contrib import admin

from .models import Experiment, Dataset, DataSource, DatasetColumn


@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    exclude = ['id']
    readonly_fields = ['created_at', 'updated_at', 'name']


@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    exclude = ['id']
    readonly_fields = ['created_at', 'updated_at', 'name', 'user']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ExperimentAdmin, self).save_model(request, obj, form, change)


@admin.register(Dataset)
class DatasetAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    exclude = ['id']
    readonly_fields = ['created_at', 'updated_at', 'name']


@admin.register(DatasetColumn)
class DatasetColumnAdmin(admin.ModelAdmin):
    date_hierarchy = 'updated_at'
    exclude = ['id']
    readonly_fields = ['created_at', 'updated_at', 'name']
