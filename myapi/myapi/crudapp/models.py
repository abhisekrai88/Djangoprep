from django.db import models
from django.db.models.expressions import When

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=100)

class Belonging(models.Model):
    name = models.CharField(max_length=100)

class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    When = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)