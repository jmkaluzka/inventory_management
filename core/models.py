from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser
from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=50, blank=True)
    path = models.FileField(upload_to='documents', blank=True)


class Device(models.Model):
    # producer = models.CharField(max_length=50)
    device_name = models.CharField(max_length=300, blank=True, null=True)
    sn = models.CharField(max_length=10, primary_key=True, editable=False)
    floor = models.PositiveIntegerField(blank=True, null=True)
    room = models.PositiveIntegerField(blank=True, null=True)
    # model = models.CharField(max_length=50, default="model")
    # production_year = models.IntegerField()


class CustomUser(AbstractBaseUser):

    name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.email

