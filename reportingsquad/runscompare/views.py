from django.views.generic.list import ListView
from django.shortcuts import render, render_to_response
from .models import TestRun, TestCaseStatus
from django.template import RequestContext


def index(request):
    return render(request, 'runscompare/comp.html')


def compareruns(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    query_newrun = TestRun.objects.filter(run_id='2')

    rows = {}

    dict = {'foo': 'bar'}
    dict['foo2'] = 'bar2'

    list = [1, 2, 3]

    status_not_executed = TestCaseStatus()
    status_not_executed.name = 'n/a'

    for new_run in query_newrun:
        old_run = TestRun.objects.filter(run_id='1', test_id=new_run.test_id)
        if old_run: #if test_id found in old run
            for old_run_item in old_run:
                rows[new_run.test_id.id] = [new_run.test_id.name, new_run.status, 0,  old_run_item.status, 0]
        else: #if test_id not found in old run - set status to not executed
            rows[new_run.test_id.id] = [new_run.test_id.name, new_run.status, 0, status_not_executed, 0]
        pass

    context_dict = {'newrun': query_newrun, 'rows': rows, 'dict': dict, 'list': list}

    # Render the response and send it back!
    return render(request, 'runscompare/comp.html', context_dict, context)
