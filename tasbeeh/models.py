from django.db import models
from django.db.models.base import Model
 
class Zekr(models.Model):
    name = models.CharField(max_length=100)
    counter = models.IntegerField(default=0)
    def __str__(self):
        return self.name