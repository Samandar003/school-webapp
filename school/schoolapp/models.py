from django.db import models
from django.urls import reverse

# Create your models here.

class Students(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  grade = models.IntegerField(default=1)
  age = models.IntegerField(default=6)
  
  def __str__(self):
    return self.first_name + '  ' + self.last_name
  def get_absolute_url(self):
      return reverse("student_detail", args=[str(self.pk)])
  

class Teachers(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  age = models.IntegerField(default=18)

  def __str__(self):
    return self.first_name + '  ' + self.last_name
  def get_absolute_url(self):
      return reverse("subject_detail", args=[str(self.pk)])
  
  
class Subjects(models.Model):
  name = models.CharField(max_length=50)
  teachers = models.ManyToManyField(Teachers)
  students = models.ManyToManyField(Students)
  
  def __str__(self):
    return self.name
  def get_absolute_url(self):
      return reverse("subject_detail", args=[str(self.pk)])
      
