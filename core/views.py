import csv
from django.http import HttpResponseRedirect
from django.shortcuts import render
import os
from .forms import UploadFileForm

def index(request):
    return render(request, 'core/index.html',{})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'core/upload.html',{'form':form})

def handle_uploaded_file(f):
    print('handle')
    csvfile = ''
    for chunk in f.chunks():
        csvfile += chunk.decode(encoding='UTF-8')
    print(csvfile)
    filereader = csv.reader(csvfile, delimiter=',')
    for row in filereader:
        print(', '.join(row))
    #f.read()