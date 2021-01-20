from django.db.models import manager
from simplecrm.crmapp.models import INDCHOICES
from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User


# Create your models here.
INDCHOICES = (
    ('MANAGEMENT', 'MANAGEMENT'),
    ('BUSINESS DEVELOPMENT', 'BUSINESS DEVELOPMENT'),
    ('HUMAN RESOURCES', 'HUMAN RESOURCES'),
    ('PRODUCT MANAGEMENT', 'PRODUCT MANAGEMENT'),
)

PERFGRADE = (
    ('EXCELLENT', 'EXCELLENT'),
    ('GOOD', 'GOOD'),
    ('AVERAGE', 'AVERAGE'),
    ('POOR', 'POOR')
)

class Employee(models.Model):
    name = models.CharField("Employee Name", max_length= 60, blank = True, null = True)
    gender = models.CharField("Gender (M/F)", max_length=1, blank = True, null = True)
    dob = models.DateField("Date of Birth", blank = True, null = True)
    joined = models.DateField("Joined Date", blank = True, null = True)
    salary = MoneyField("Salary", max_digits=14, decimal_places=2, default_currency='SGD', blank = True, null = True)
    Active = models.BooleanField(default=False)
    department = models.CharField("Department", max_length=50, choices=INDCHOICES, blank = True, null = True)

    def __str__(self):
        return self.name

class Department(models.Model):
    department = models.CharField("Department", max_length=50, choices=INDCHOICES, blank = True, null = True)
    manager = models.ForeignKey("Manager", User, related_name='employee_name')
    Active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.department

class Appraisal(models.Model):
    name = models.ForeignKey("Employee", User, related_name='employee_name')
    grade = models.CharField("Performace Grade", choices=PERFGRADE, max_length=20, blank = True, null = True)
    year = models.IntegerField("Year", max_length=4, blank=True, null=True)

    def __str__(self):
        return self.name