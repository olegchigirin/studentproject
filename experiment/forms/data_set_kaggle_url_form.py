from django import forms


class DataSetKaggleURLForm(forms.Form):
    kaggle_url = forms.URLField(max_length=200)

    def clean(self):
        cleaned_data = super(DataSetKaggleURLForm, self).clean()
        kaggle_url = cleaned_data.get('kaggle_url')
        if not kaggle_url:
            raise forms.ValidationError('You have to write something!')
