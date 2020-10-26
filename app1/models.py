from django.db import models
import datetime
from django.utils import timezone

class MyModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.MyModel_text