from django.db import models
from adminsapp.models import *
# Create your models here.

class Requirements(models.Model):
    email=models.EmailField()
    projects=models.ForeignKey(Project,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=350)
    priority=models.CharField(max_length=300)
    ndatetime = models.DateTimeField(auto_now=True)


class Testcase(models.Model):
    requirements=models.CharField(max_length=350)
    project_name=models.CharField(max_length=350)
    module_name=models.CharField(max_length=350)
    senario=models.CharField(max_length=350)
    description=models.CharField(max_length=350)
    input_data=models.CharField(max_length=350)
    type_of_exception=models.CharField(max_length=350)
    pre_condition=models.CharField(max_length=350)
    expected_actual_result=models.CharField(max_length=350)
    status=models.CharField(max_length=300)
    date_of_creation=models.DateField(auto_now=True)
    tester_email=models.EmailField()
    teststeps = models.CharField(max_length=100)
    priority=models.CharField(max_length=300)
    comments = models.CharField(max_length=100, default="Empty")



class Bug(models.Model):
    title=models.CharField(max_length=100)
    testcase_id=models.IntegerField()
    description=models.CharField(max_length=350)
    test_path=models.CharField(max_length=300)
    screenshot=models.ImageField(upload_to="images/")
    sevearity=models.CharField(max_length=300)
    priority=models.CharField(max_length=300)
    status=models.CharField(max_length=300)
    date=models.DateField(auto_now=True)
    tested_by_email=models.EmailField()
    reproductionsteps=models.CharField(max_length=350)
    environment=models.CharField(max_length=350)
    browser=models.CharField(max_length=350)
    os=models.CharField(max_length=350)
    errordetails=models.CharField(max_length=350)

    developer_email=models.CharField(max_length=350)
