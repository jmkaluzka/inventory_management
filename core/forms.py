import os
from django import forms
from django.core.exceptions import ValidationError


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean(self):
        cleaned_data = super(UploadFileForm, self).clean()
        file = cleaned_data.get('file')
        name, extension = os.path.splitext(file.name)
        if extension[1:] != 'csv':
            raise forms.ValidationError('Wrong format, you need a csv file')