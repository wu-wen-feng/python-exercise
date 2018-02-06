from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test/$', views.test),
    url(r'^index/$', views.index, name="index"),
    url(r'^detail/(?P<id>\d+)$', views.detail, name="detail"),
    url(r'^edit/(?P<id>\d+)$', views.edit, name="edit"),
    url(r'^save$', views.save, name="save"),
]
