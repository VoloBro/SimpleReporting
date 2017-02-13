from django.conf.urls import url
from django.views.generic import ListView
from .models import TestRun

# urlpatterns = [
#     url(r'^$', ListView.as_view(queryset=TestRun.objects.all(), template_name="runscompare/comp.html"))
# ]


for p in TestRun.objects.raw('SELECT * FROM runscompare_testrun'):
    print(p)