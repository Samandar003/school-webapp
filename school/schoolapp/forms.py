from django import forms
from django.forms import ModelForm
from .models import Students, Teachers, Subjects

class StudentsForm(forms.Form):
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  grade = forms.IntegerField(min_value=1)  
  age = forms.IntegerField(min_value=6)
  
class TeachersForm(forms.Form):
  first_name = forms.CharField(max_length=50, required=True)
  last_name = forms.CharField(max_length=50)
  age = forms.IntegerField(min_value=18)

class SubjectsForm(ModelForm):
  class Meta:
    model = Subjects
    fields = '__all__'
    