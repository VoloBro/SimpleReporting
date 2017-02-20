from django.conf.urls import url
from django.views.generic import ListView
from . import views
from .models import TestCase, TestRun

urlpatterns = [
    url(r'^$', views.testexecution),
    url(r'^comp/$', views.compareruns),
    url(r'^filter/$', views.filertable)
]