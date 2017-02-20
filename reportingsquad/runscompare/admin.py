from django.contrib import admin
from .models import *

admin.site.register(TestCase)
admin.site.register(TestRun)
admin.site.register(TestCaseStatus)
admin.site.register(TestExecution)


