import csv
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import os
from .forms import UploadFileForm
from .models import Document, Device

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print(request.FILES['csv_file'])
            n = ''.join([i for i in str(request.FILES['csv_file']) if i.isalnum()])
            newfile = Document.objects.create(name = n, path = request.FILES['csv_file'])
            print(newfile.id)
            return HttpResponseRedirect('/uploaded/%d/' % newfile.id)
    else:
        form = UploadFileForm()
    return render(request, 'core/upload.html',{'form':form})


def uploaded(request, file_id=None):
    file = Document.objects.get(id=file_id)
    print("file",file_id)
    f = open(str(file.path), 'r')
    print(type(f))
    datareader = csv.reader(f, delimiter=',')

    valid = False
    devices = []
    for row in datareader:
        name = row[0]

        if name == "Nazwa":
            valid = True
        elif name == "":
            valid = False
        else:
            if valid:
                Device.objects.create(device_name=name)
                devices.append(name)
    print("count",len(devices))
    return render(request, 'core/uploaded.html',{'devices':devices})

def list_devices(request):
    return render(request, 'core/devices.html', {'devices':Device.objects.all()})