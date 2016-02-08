import os
from django import forms


class UploadFileForm(forms.Form):

    csv_file = forms.FileField(
        label='Select a file',
        help_text='Only csv files'
    )

    def clean(self):
        cleaned_data = super(UploadFileForm, self).clean()
        file = cleaned_data.get('csv_file')
        name, extension = os.path.splitext(file.name)
        if extension[1:] != 'csv':
            raise forms.ValidationError('Wrong format, you need a csv file')
