from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=200)
    classes=models.CharField(max_length=200)
    roll_number=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=200)

    def __str__(self):
        return self.name