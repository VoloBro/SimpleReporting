from django.views.generic.list import ListView
from django.shortcuts import render, render_to_response
from .models import *
from django.template import RequestContext

def index(request):
    return render(request, 'runscompare/comp.html')

def compareruns(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    query_newrun = TestRun.objects.filter(run_id='2')
    query_oldrun = TestRun.objects.filter(run_id='3')

    rows = {}

    dict = {'foo': 'bar'}
    dict['foo2'] = 'bar2'

    list = [1, 2, 3]

    status_not_executed = TestCaseStatus()
    status_not_executed.name = 'n/a'

    for new_run in query_newrun:
        old_run_byid = query_oldrun.filter(test_id=new_run.test_id)
        if old_run_byid: #if test_id found in old run
            for old_run_item in old_run_byid:
                rows[new_run.test_id.id] = [new_run.test_id.name, new_run.status, 0,  old_run_item.status, 0]
        else: #if test_id not found in old run - set status to not executed
            rows[new_run.test_id.id] = [new_run.test_id.name, new_run.status, 0, status_not_executed, 0]

    for old_run in query_oldrun:
        if old_run.test_id.id not in rows.keys():
            rows[old_run.test_id.id] = [old_run.test_id.name, status_not_executed, 0, old_run.status, 0]


    context_dict = {'newrun': query_newrun, 'rows': rows, 'dict': dict, 'list': list}

    # Render the response and send it back!
    return render(request, 'runscompare/comp.html', context_dict, context)

def testexecution(request):
    context = RequestContext(request)

    query_runs = TestExecution.objects.all()[:25]

    context_dict = {'runs': query_runs}

    return render(request, 'runscompare/testexecution.html', context_dict)

def filertable(request):
    return render(request, 'runscompare/filtertable.html')