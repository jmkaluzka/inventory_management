import os
from django import forms
from django.forms import ModelForm

from core.models import Device


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


class DeviceForm(ModelForm):

    class Meta:
        model = Device
        exclude = ['sn']

    def clean(self):
        cleaned_data = super(DeviceForm, self).clean()
        floor = cleaned_data.get("floor")
        if floor > 5:
            raise forms.ValidationError("Floor cannot be bigger than 5")
        room = cleaned_data.get("room")
        if int(room/100) != floor:
            raise forms.ValidationError("Room " + str(room) +
                                        " is not on the floor no." +
                                        str(floor))
