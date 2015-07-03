from django.shortcuts import render
from .forms import UploadFileForm

def index(request):
	return render(request, 'core/index.html',{})

def upload(request):
	form = UploadFileForm()
	return render(request, 'core/upload.html',{'form':form})