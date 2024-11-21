from django.db import models
from employeeapp.models import Bug,Testcase
# Create your models here.

class Contact(models.Model):
    message=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)

class Task(models.Model):
    manager_email=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    employee_email=models.EmailField()
    project=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    enddate=models.DateField()
