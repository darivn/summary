from django.conf import settings
from django.db import models

class Background (models.Model):
    institution_name = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    faculty = models.CharField(max_length=300)
    specialization = models.CharField(max_length=200)
    level = models.CharField(max_length=150)
    year_start = models.IntegerField()
    year_end = models.IntegerField()


    def __str__(self):
        return self.institution_name