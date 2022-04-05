from django.db import models
from datetime import datetime


class Order(models.Model):
    client = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    amount = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now,blank=True)
  
    def __str__(self):
        return self.client
