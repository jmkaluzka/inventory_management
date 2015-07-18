import os
from django import forms
from .models import Document
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, ButtonHolder


class UploadFileForm(forms.ModelForm):
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