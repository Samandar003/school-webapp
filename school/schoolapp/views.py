from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic.base import View
from django.views.generic.list import ListView
from .forms import StudentsForm, TeachersForm, SubjectsForm
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .models import Students, Teachers, Subjects



class StudentsView(ListView):   
  def get(self, request):
    students = Students.objects.all()
    if students:
      search = request.GET.get('search')
      if search:
        if Students.objects.filter(first_name__contains=search):
          students = Students.objects.filter(first_name__contains=search)
        elif Students.objects.filter(last_name__contains=search):
          students = Students.objects.filter(last_name__contains=search)
        else:
          students = Students.objects.all()
        return render(request, 'students_list.html', {'students':students, 'search':search})
      else:
        students = Students.objects.all()
        return render(request, 'students_list.html', {'students':students})
    else:
      return HttpResponse('There is no students')

class StudentDetailView(DetailView):
  def get(self, request, pk):
    student = Students.objects.get(id=pk)
    return render(request, 'student_detail.html', {'student':student})
      
class TeachersView(ListView):
  def get(self, request):
    teachers = Teachers.objects.all()
    if teachers:
      search = request.GET.get('search')
      if search:
        if Teachers.objects.filter(first_name__contains=search):
           teachers = Teachers.objects.filter(first_name__contains=search) 
        elif Teachers.objects.filter(last_name__contains=search):
            teachers = Teachers.objects.filter(last_name__contains=search)
        else:
            teachers = Teachers.objects.all()
        return render(request, 'teachers_list.html', {'teachers':teachers, 'search':search})
      else:
        return render(request, 'teachers_list.html', {'teachers':teachers})
    else:
      return HttpResponse('There is no teachers')
  
class TeacherDetailView(DetailView):
  def get(self, request, pk):
    teacher = Teachers.objects.get(id=pk)
    if teacher:
      return render(request, 'teacher_detail.html', {'teacher':teacher})
    
class SubjectsView(ListView):
  def get(self, request):
    subjects = Subjects.objects.all()
    if subjects:
      search = request.GET.get('search')
      if search:
        if Subjects.objects.filter(name__contains=search):
          subjects = Subjects.objects.filter(name__contains=search)
        else:
          subjects = Subjects.objects.all()
        return render(request, 'subjects_list.html', {'subjects':subjects, 'search':search})
      return render(request, 'subjects_list.html', {'subjects':subjects})
    else:
      return HttpResponse('There is no subjects')     

class SubjectDetailView(DetailView):
  def get(self, request, pk):
    subject = Subjects.objects.get(id=pk)
    if subject:
      return render(request, 'subject_detail.html', {'subject':subject})
    else:
      return HttpResponse('There is no subjects')  
   
class Student_search(View):
  def get(self, request):
    students = Students.objects.all()
    if students:
      search = request.GET.get('search')
      if search:
        students = Students.objects.filter(first_name=search)
        return render(request, 'students_list.html', {'students':students})
      else:
        return render(request, 'students_list.html', {'students':students})
    else:
      return HttpResponse('There is no students!')
      
class Teacher_search(View):
  def get(self, request):
    teachers = Teachers.objects.all()
    if teachers:
      search = request.GET.get('search')
      if search:
        teachers = Teachers.objects.filter(first_name=search)
        return render(request, 'teachers_list.html', {'teachers':teachers})
      else:
        return render(request, 'teachers_list.html', {'teaachers':teachers})
    else:
      return HttpResponse('There is no teachers')
        
class Subject_search(View):
  def get(self, request):
    subjects = Subjects.objects.all()
    if subjects:
      search = request.GET.get('search')
      if search:
        subjects = Subjects.objects.filter(name=search)
        return render(request, 'subjects_list.html', {'subjects':subjects})
      else:
        return render(request, 'subjects_list.html', {'subjects':subjects})
    else:
      return HttpResponse('There is no subjects')
    
class StudentCreateView(CreateView):
  model = Students
  template_name = 'student_create.html'
  fields = '__all__'
  
class TeacherCreateView(CreateView):
  model = Teachers
  template_name = 'teacher_create.html'
  fields = '__all__'

class Subject_create(CreateView):
  model = Subjects
  template_name = 'subject_create.html'
  fields = '__all__'

# def homepageview(request):
#   return render(request, 'home.html')


# def studentsview(request):
#   students = Students.objects.all()
#   if students:
#     search = request.GET.get('search')
#     if search:
#       if Students.objects.filter(first_name__contains=search):
#         students = Students.objects.filter(first_name__contains=search)
#       elif Students.objects.filter(last_name__contains=search):
#         students = Students.objects.filter(last_name__contains=search)
#       else:
#         students = Students.objects.all()
#       return render(request, 'students_list.html', {'students':students, 'search':search})
#     else:
#       students = Students.objects.all()
#       return render(request, 'students_list.html', {'students':students})
#   else:
#     return HttpResponse('There is no students')

# def student_detailview(request, pk):
#   student = Students.objects.get(id=pk)
#   return render(request, 'student_detail.html', {'student':student})

# def student_search(request):
#   students = Students.objects.all()
#   if students:
#     search = request.GET.get('search')
#     if search:
#       students = Students.objects.filter(first_name=search)
#       return render(request, 'students_list.html', {'students':students})
#     else:
#       return render(request, 'students_list.html', {'students':students})
#   else:
#     return HttpResponse('There is no students!')

# def teachersview(request):
#   teachers = Teachers.objects.all()
#   if teachers:
#     search = request.GET.get('search')
#     if search:
#       if Teachers.objects.filter(first_name__contains=search):
#          teachers = Teachers.objects.filter(first_name__contains=search) 
#       elif Teachers.objects.filter(last_name__contains=search):
#           teachers = Teachers.objects.filter(last_name__contains=search)
#       else:
#           teachers = Teachers.objects.all()
#       return render(request, 'teachers_list.html', {'teachers':teachers, 'search':search})
#     else:
#       return render(request, 'teachers_list.html', {'teachers':teachers})

# def teacher_detailview(request, pk):
#   teacher = Teachers.objects.get(id=pk)
#   if teacher:
#     return render(request, 'teacher_detail.html', {'teacher':teacher})

# def teacher_search(request):
#   teachers = Teachers.objects.all()
#   if teachers:
#     search = request.GET.get('search')
#     if search:
#       teachers = Teachers.objects.filter(first_name=search)
#       return render(request, 'teachers_list.html', {'teachers':teachers})
#     else:
#       return render(request, 'teachers_list.html', {'teaachers':teachers})
#   else:
#     return HttpResponse('There is no teachers')

# def subjectsview(request):
#   subjects = Subjects.objects.all()
#   if subjects:
#     search = request.GET.get('search')
#     if search:
#       if Subjects.objects.filter(name__contains=search):
#         subjects = Subjects.objects.filter(name__contains=search)
#       else:
#         subjects = Subjects.objects.all()
#       return render(request, 'subjects_list.html', {'subjects':subjects, 'search':search})
#     return render(request, 'subjects_list.html', {'subjects':subjects})
#   else:
#     return HttpResponse('There is no subjects')

# def subject_detailview(request, pk):
#   subject = Subjects.objects.get(id=pk)
#   teachers = Subjects.teachers
#   students = Subjects.students
#   if subject:
#     return render(request, 'subject_detail.html', {'subject':subject, 'teachers':teachers,
#                                                    'students':students})
#   else:
#     return HttpResponse('There is no subjects')

# def subject_search(request):
#   subjects = Subjects.objects.all()
#   if subjects:
#     search = request.GET.get('search')
#     if search:
#       subjects = Subjects.objects.filter(name=search)
#       return render(request, 'subjects_list.html', {'subjects':subjects})
#     else:
#       return render(request, 'subjects_list.html', {'subjects':subjects})
#   else:
#     return HttpResponse('There is no subjects')

# def student_create(request):
#   if request.method == 'GET':
#     form = StudentsForm()
#   else:
#     form = StudentsForm(request.POST)
#     if form.is_valid():
#       data = form.cleaned_data
#       stud = Students.objects.create(
#         first_name = data['first_name'],
#         last_name = data['last_name'],
#         grade = data['grade'],
#         age = data['age'],
#       )
#       return redirect('students_list')
#   return render(request, 'student_create.html', {'form':form})

# def subject_create(request):
#   if request.method == 'GET':
#     form = SubjectsForm()
#   else:
#     form = SubjectsForm(request.POST)
#     if form.is_valid:
#         form.save()
#         return redirect('subjects')
#   return render(request, 'subject_create.html', {'form':form})

# def teacher_create(request):
#   if request.method == 'GET':
#     form = TeachersForm()
#   else:
#     form = TeachersForm(request.POST)
#     if form.is_valid():
#       data = form.cleaned_data
#       teach = Teachers.objects.create(
#         first_name = data['first_name'],
#         last_name = data['last_name'],
#         age = data['age'],
#       )    
#       return redirect('teachers')
#   return render(request, 'teacher_create.html', {'form':form})
