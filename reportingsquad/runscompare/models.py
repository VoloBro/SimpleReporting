from django.db import models

# Create your models here.

class TestCaseStatus(models.Model):
    name = models.CharField(default='n/a', max_length=50)
    def __str__(self):
        return self.name


class TestCase(models.Model):
    id = models.CharField(unique=True, max_length=100, primary_key=True)
    name = models.CharField(default='n/a', max_length=200)

    def __str__(self):
        return self.name


class TestRun(models.Model):
    test_id = models.ForeignKey(TestCase)
    run_id = models.CharField(max_length=100, default='0')
    datetime = models.DateTimeField()
    status = models.ForeignKey(TestCaseStatus)
    messages = models.CharField(default='n/a', max_length=500)

    def __str__(self):
        return "%s %s" % (self.run_id, self.test_id.name)

class TestExecution(models.Model):
    run_id = models.CharField(max_length=100, default='0', primary_key=True)
    suite_name = models.CharField(max_length=100, default='Test suite name')
    duration = models.PositiveIntegerField()
    comments = models.CharField(max_length=255, default='no run comments')

    def __str__(self):
        return "[%s] %s - %s" % (self.run_id, self.suite_name, self.comments)