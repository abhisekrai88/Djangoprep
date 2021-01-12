# models.py
from django.db import models
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self
        
class todo(models.Model):
    task = models.CharField(max_length=60)
    priority = models.CharField(max_length=60)
    duedate = models.DateField(null=True)
    def __str__(self):
        return self        

