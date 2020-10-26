from django.db import models
import datetime
from django.utils import timezone

class MyModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self .title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class List(models.Model):
    title = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)