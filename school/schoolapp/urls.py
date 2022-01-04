from django.urls import path
from django.views.generic import TemplateView
from .views import (StudentsView,
                    StudentDetailView, 
                    TeachersView, 
                    TeacherDetailView,
                    SubjectsView,
                
                    SubjectDetailView,
                    Student_search,
                    Teacher_search,
                    Subject_search,
                    StudentCreateView,
                    TeacherCreateView,
                    Subject_create
)
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('students/', StudentsView.as_view(), name='students_list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('teachers/', TeachersView.as_view(), name='teachers'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('subjects/', SubjectsView.as_view(), name='subjects'),
    path('subject/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('student/', Student_search.as_view(), name='student_search'),
    path('teacher/', Teacher_search.as_view(), name='teacher_search'),
    path('subject/', Subject_search.as_view(), name='subject_search'),
    path('student/create/', StudentCreateView.as_view(), name='student_create'),
    path('teacher/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('subject/create/', Subject_create.as_view(), name='subject_create'),
]
