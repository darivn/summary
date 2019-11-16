from django.conf import settings
from django.db import models
import datetime

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

    class Meta:
        ordering = ['year_start']

class Experience (models.Model):
    position = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    area = models.CharField(max_length=300)
    responsibilities = models.CharField(max_length=300)
    time_start = models.DateField(default=datetime.date.today())
    time_end = models.DateField(default=datetime.date.today(), null=True, blank=True)

    def __str__(self):
        return self.position

    class Meta:
        ordering = ['time_start']