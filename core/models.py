from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, AbstractBaseUser, AbstractUser, \
    PermissionsMixin
from django.db import models
from django.db.models import SET_NULL


class Document(models.Model):
    name = models.CharField(max_length=50, blank=True)
    path = models.FileField(upload_to='documents', blank=True)


class Student(models.Model):
    number = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)


class Device(models.Model):
    # producer = models.CharField(max_length=50)
    device_name = models.CharField(max_length=300, blank=True, null=True)
    sn = models.CharField(max_length=10, primary_key=True, editable=False)
    floor = models.PositiveIntegerField(blank=True, null=True)
    room = models.PositiveIntegerField(blank=True, null=True)
    available = models.BooleanField(default=True)
    student = models.ForeignKey(Student, blank=True, null=True,
                                on_delete=SET_NULL)
    # model = models.CharField(max_length=50, default="model")
    # production_year = models.IntegerField()


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name=None, last_name=None,
                    password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.email
