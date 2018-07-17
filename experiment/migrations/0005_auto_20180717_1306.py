# Generated by Django 2.0.5 on 2018-07-17 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0004_auto_20180717_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasetcolumn',
            name='datatype',
            field=models.CharField(choices=[('object', 'object'), ('int64', 'int64'), ('float', 'float64'), ('bool', 'bool'), ('datetime64', 'datetime64'), ('timedelta[ns]', 'timedelta[ns]'), ('category', 'category')], max_length=50, verbose_name='Column datatype'),
        ),
    ]
