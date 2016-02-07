from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^devices/$', views.list_devices, name='list_devices'),
    url(r'^upload/$', views.upload_file),
    url(r'^uploaded/(?P<file_id>\d+)/$', views.uploaded),
    url(r'^profile/$', views.profile_page, name='profile_page'),
]
