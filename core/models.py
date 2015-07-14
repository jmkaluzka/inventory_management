from django.db import models
from .forms import UploadFileForm

class ModelWithFileField(models.Model):
    name = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    mail = models.EmailField()

class Employee(User):
    password = models.CharField(max_length=50)

class Student(User):
    students_number = models.IntegerField()
    remarks = models.TextField(max_length=300)

class Device(models.Model):
    producer = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    production_year = models.IntegerField()
