from django.db import models
from datetime import datetime


class Design(models.Model):
    designer = models.CharField(max_length=100, default='Senper Graphics')
    item = models.CharField(max_length=100)
    client = models.CharField(max_length=200)
    price = models.IntegerField
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to = 'designs/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'designs/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to = 'designs/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to = 'designs/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to = 'designs/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.client