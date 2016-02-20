import csv
import random
import string

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import UploadFileForm, DeviceForm
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
    return render(request, 'core/form.html', {'form': form})


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
    floor = request.POST.get('floor', None)
    devices = Device.objects.all()
    if floor:
        devices = devices.filter(floor=floor)
    return render(request, 'core/list_devices.html',
                  {'devices': devices})


def show_device(request, pk):
    devices = Device.objects.filter(pk=pk)
    if not devices:
        message = "Sorry, device not found"
        return render(request, 'core/message.html', {'message': message})
    elif len(devices) != 1:
        message = "More than one device of the some id, something is wrong"
        return render(request, 'core/message.html', {'message': message})
    else:
        return render(request, 'core/device.html', {'devices': devices})


def delete_device(request, pk):
    Device.objects.filter(pk=pk).delete()
    message = "Device " + pk + " deleted."
    return render(request, 'core/message.html', {'message': message})


def edit_device(request, pk):
    try:
        device = Device.objects.get(pk=pk)
    except ObjectDoesNotExist as e:
        message = "Sorry, device not found"
        return render(request, 'core/message.html', {'message': message})
    if request.method == 'POST':
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            print(device.floor)
            device = form.save()
            print(device.floor)
            return redirect('device', pk=pk)
        else:
            print(form.errors)
    else:
        form = DeviceForm(instance=device)
    return render(request, 'core/form.html', {'form': form})


def profile_page(request):
    return render(request, 'core/profile.html', {'user': request.user})


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
