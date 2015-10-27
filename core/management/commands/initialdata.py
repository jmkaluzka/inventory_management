from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    def handle(self, *arg, **options):
        stuff = Group.objects.get_or_create(name="stuff")[0]
        #print(stuff.name)
        print("group %s created" % stuff.name)
        stuff.permissions.add(Permission.objects.get(codename="add_device"))
        stuff.permissions.add(Permission.objects.get(codename="change_device"))
        stuff.permissions.add(Permission.objects.get(codename="delete_device"))
        print("permissions added")