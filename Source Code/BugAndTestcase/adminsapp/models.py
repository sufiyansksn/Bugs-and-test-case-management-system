from django.db import models

# Create your models here.

class Admins(models.Model):
    username = models.CharField(max_length=50)
    password = models.IntegerField()

class Employee(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    dateofjoin=models.DateField()
    salary=models.IntegerField()
    gender=models.CharField(max_length=100)
    role=models.CharField(max_length=100)

class Project(models.Model):
    title=models.CharField(max_length=100)
    code=models.CharField(max_length=100)
    technology=models.CharField(max_length=100)
    domain=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    fromdate=models.DateField()
    todate=models.DateField()
    manager=models.CharField(max_length=100)

class News(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now=True)
