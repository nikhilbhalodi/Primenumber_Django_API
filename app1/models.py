from django.db import models

# Create your models here.
# using 3 fields create model

class PrimeNumber(models.Model):
    in1 = models.PositiveIntegerField()
    in2 = models.PositiveIntegerField()
    out = models.TextField(max_length=400)
    
