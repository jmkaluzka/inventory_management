import csv
import random
import string

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import UploadFileForm
from .models import Document, Device


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            n = ''.join(
                    [i for i in str(request.FILES['csv_file']) if i.isalnum()])
            newfile = Document.objects.create(name=n,
                                              path=request.FILES['csv_file'])
            return HttpResponseRedirect('/uploaded/%d/' % newfile.id)
    else:
        form = UploadFileForm()
    return render(request, 'core/upload.html', {'form': form})


def uploaded(request, file_id=None):
    file = Document.objects.get(id=file_id)
    f = open(str(file.path), 'r')
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
                floor = generate_floor(5)
                d = Device.objects.create(device_name=name, sn=generate_sn(10),
                                          floor=floor,
                                          room=generate_room(floor, 20))
                devices.append(d)
    return render(request, 'core/uploaded.html', {'devices': devices})


def list_devices(request):
    if request.POST["floor"].isdigit():
        devices = Device.objects.filter(floor=request.POST["floor"])
    else:
        devices = Device.objects.all()
    return render(request, 'core/list_devices.html',
                  {'devices': devices})


def profile_page(request):
    return render(request, 'core/profile.html', {})


def index(request):
    return render(request, 'index.html', {})
    # return HttpResponse(request, 'index.html', {})


def generate_sn(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits)
                   for i in range(n))


def generate_floor(n):
    return random.randint(1, n)


def generate_room(floor, n):
    return random.randint(1, n) + floor*100
