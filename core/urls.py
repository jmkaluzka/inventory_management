from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.list_devices),
    url(r'^upload/$', views.upload_file),
    url(r'^uploaded/(?P<file_id>\d+)/$', views.uploaded),
]
