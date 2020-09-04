from django.db import models
from datetime import datetime

class Tutorial(models.Model):
    course_name = models.CharField(max_length=100)
    course = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.course_name
