from __future__ import unicode_literals

from django.db import models

# Create your models here.

class entry(models.model):
    entry_date = models.DateField()
    particulars = models.CharField(max_length = 100)
    amount = models.
