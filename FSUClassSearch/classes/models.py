from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Student(models.Model):
    FSUID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.FSUID 

class Professor(models.Model):
    FSUID = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    office = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.FSUID.username

class Class(models.Model):
    subject_id = models.CharField(max_length=3)
    number_id = models.CharField(max_length=4)
    section = models.CharField(max_length=4)
    semester = models.CharField(max_length=6)
    year = models.IntegerField()
    professor_id = models.ForeignKey(User, on_delete=models.CASCADE)
    CSBS_Req = models.BooleanField(default=False, blank=True)
    CSBS_Elec = models.BooleanField(default=False, blank=True)
    CSBA_Req = models.BooleanField(default=False, blank=True)
    CSBA_Elec = models.BooleanField(default=False, blank=True)
    time_start = models.TimeField(null=True, blank=True)
    time_end = models.TimeField(null=True, blank=True)
    date_start = models.DateField(default=date(2021, 1, 6))
    date_end = models.DateField(default=date(2021, 4, 23))
    enrollment_capacity = models.IntegerField()
    enrollment_number = models.IntegerField(default=0)
    location = models.CharField(max_length=10, null=True, blank=True)
    hasRecitation = models.BooleanField(default=False)
    recitation_time_start = models.TimeField(null=True, blank=True)
    recitation_time_end = models.TimeField(null=True, blank=True)
    recitation_location = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.subject_id + self.number_id + '-' + self.section

