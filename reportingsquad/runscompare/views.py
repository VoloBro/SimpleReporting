from django.views.generic.list import ListView
from django.shortcuts import render
from .models import TestRun


def index(request):
    return render(request, 'runscompare/comp.html')
class CompareListView(ListView):

    model = TestRun

    def get_context_data(self, **kwargs):
        context = super(CompareListView, self).get_context_data(**kwargs)
        return context

        # out = {}
        # # Start with run_id=1
        # a = TestRun.objects.filter(run_id="1").select_related(
        #     'test_id', 'status').prefetch_related(
        #     'test_id__testrun_set', 'test_id__testrun_set__status')
        #
        # # For each, get related
        # for i in a:
        #     b = i.test_id.testrun_set.filter(run_id="2")
        #     print(i.test_id, i.status, [j.status for j in b])