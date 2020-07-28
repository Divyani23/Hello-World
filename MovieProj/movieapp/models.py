from django.db import models

# Create your models here.
class AbtMovie(models.Model):
    mname=models.CharField(max_length=10);
    mrating=models.CharField(max_length=10);
    mcast=models.CharField(max_length=10);
    mdate=models.DateField();
