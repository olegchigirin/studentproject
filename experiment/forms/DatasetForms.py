from django import forms

from experiment.models import Dataset


class DatasetLocalCreateForm(forms.ModelForm):
    class Meta:
        model = Dataset
        exclude = ['experiment', 'id']


class DatasetKaggleURLForm(forms.Form):
    kaggle_url = forms.URLField(max_length=200)

    def clean(self):
        cleaned_data = super(DatasetKaggleURLForm, self).clean()
        kaggle_url = cleaned_data.get('kaggle_url')
        if not kaggle_url:
            raise forms.ValidationError('You have to write something!')


class DatasetKaggleCreateForm(forms.ModelForm):
    class Meta:
        model = Dataset
        exclude = ['experiment', 'data_file', 'description', 'label']


class DatasetKaggleFileForm(forms.Form):
    files = forms.ChoiceField()
    kaggle_url = forms.CharField

    def __init__(self, *args, **kwargs):
        self.files.widget = forms.Select
        self.files.choices = kwargs['files']
        self.kaggle_url = kwargs['kaggle_url']
        super(DatasetKaggleFileForm, self).__init__(*args, **kwargs)
