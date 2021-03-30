from django.db import models

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=30)
    s_age = models.IntegerField(default=1)

    def __str__(self):
        return self.s_name
