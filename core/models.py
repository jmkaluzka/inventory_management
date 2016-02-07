from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager


class Document(models.Model):
    name = models.CharField(max_length=50, blank=True)
    path = models.FileField(upload_to='documents', blank=True)

'''
class Employee(User):
    password = models.CharField(max_length=50)

class Student(User):
    students_number = models.IntegerField()
    remarks = models.TextField(max_length=300)
'''


class Device(models.Model):
    # producer = models.CharField(max_length=50)
    device_name = models.CharField(max_length=300, blank=True, null=True)
    sn = models.CharField(max_length=10, primary_key=True, editable=False)
    floor = models.IntegerField(blank=True, null=True)
    room = models.IntegerField(blank=True, null=True)
    # model = models.CharField(max_length=50, default="model")
    # production_year = models.IntegerField()
