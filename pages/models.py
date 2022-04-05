from django.db import models
from datetime import datetime

class Designer(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField()
    bio = models.CharField(max_length=100)
    about_you = models.TextField()
    work_at = models.CharField(max_length=100, blank=True)
    skill_1 = models.CharField(max_length=100, blank=True)
    skill_2 = models.CharField(max_length=100, blank=True)
    skill_3 = models.CharField(max_length=100, blank=True)
    skill_4 = models.CharField(max_length=100, blank=True)
    skill_5 = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    youtube = models.CharField(max_length=100, blank=True)
    hobbies = models.CharField(max_length=100, blank=True)
    profile = models.ImageField(upload_to= 'profile_pic/')
    join_date = models.DateTimeField(default=datetime.now)
    design_no=models.IntegerField(default=0)
        
    def __str__(self):
        return self.name


class Design(models.Model):
    # url = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    client = models.CharField(max_length=200)
    price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    designer = models.ForeignKey(Designer, on_delete=models.CASCADE )
    photo_main = models.ImageField(upload_to = 'designs/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'designs/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to = 'designs/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to = 'designs/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to = 'designs/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.client