import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class DiaryEntry(models.Model):
    entry_title = models.CharField(max_length=100, default='Merkintä')
    entry_text = models.CharField(max_length=1000)
    entry_date = models.DateTimeField('Päiväkirjamerkintä')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.entry_text
    
    def was_entered_recently(self):
        return self.entry_date >= timezone.now() - datetime.timedelta(days=1)
