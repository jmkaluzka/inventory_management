import os
from django import forms
from .models import Document

class UploadFileForm(forms.Form):

    csv_file = forms.FileField(
        label='Select a file',
        help_text='Only csv files'
    )

    def clean(self):
        cleaned_data = super(UploadFileForm, self).clean()
        file = cleaned_data.get('csv_file')
        name, extension = os.path.splitext(file.name)
        print(name,extension)
        if extension[1:] != 'csv':
            raise forms.ValidationError('Wrong format, you need a csv file')
    '''        
    class Meta:
        model = Document
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('path',placeholder=kwargs.pop('query_placeholder', 'Path to csv file')),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-lg btn-success')
            )
        )
        self.helper.form_show_labels = False
    '''