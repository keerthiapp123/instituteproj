from django.db import models

# Create your models here.
class ServisesData(models.Model):
    courseno=models.IntegerField()
    coursename=models.CharField(max_length=20)
    timings=models.CharField(max_length=20)
    startdate=models.DateField(max_length=20)
    duration=models.CharField(max_length=20)
    coursefee=models.IntegerField()
    trainername=models.CharField(max_length=20)


class FeedbackData(models.Model):
    name=models.CharField(max_length=20)
    ratings=models.IntegerField()
    comments=models.CharField(max_length=100)
    createdat=models.DateTimeField(auto_now_add=True)