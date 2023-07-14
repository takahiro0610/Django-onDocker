from django.db import models
from datetime import datetime

# Create your models here.

CHOICE = (("danger","high"),("primary","nomal"),("secondary","low"))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = CHOICE,
        default='low'
        )
    duedate = models.DateField(default=datetime.now)
    
    def __str__(self):
        return self.title