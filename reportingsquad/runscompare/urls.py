from django.conf.urls import url
from django.views.generic import ListView
from . import views
from .views import CompareListView
from .models import TestCase, TestRun


urlpatterns = [
    # url(r'^$', ListView.as_view(queryset=TestRun.objects.all(), template_name="runscompare/comp.html"))
    url(r'^$', CompareListView.as_view(template_name="runscompare/comp.html"), name="comp")
]

