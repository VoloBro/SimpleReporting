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
    run_not_executed = TestRun()
    run_not_executed.status = status_not_executed

    for testcase in query_newrun:
        old_run = TestRun.objects.filter(run_id='1', test_id=testcase.test_id)
        if old_run:
            for item in old_run:
                #rows[testcase.test_id.id] = "2"
                rows[testcase.test_id.id] = item.status
        else:
            rows[testcase.test_id.id] = run_not_executed
        pass

    context_dict = {'newrun': query_newrun, 'rows': rows, 'dict': dict, 'list': list}

    # Render the response and send it back!
    return render(request, 'runscompare/comp.html', context_dict, context)
