from django.db import models

# Create your models here.
class Students_Info(models.Model):
    name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150)
    mobile_number = models.IntegerField()
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    address = models.TextField()
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)