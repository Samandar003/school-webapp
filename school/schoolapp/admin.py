from django.contrib import admin

# Register your models here.
from .models import Students, Teachers, Subjects

# admin.site.register(Students)
# admin.site.register(Teachers)
# admin.site.register(Subjects)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
  search_fields = ('first_name', 'last_name',)
  list_display = ('first_name', 'last_name')
  list_filter = ('grade',)

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
  search_fields = ('first_name', 'last_name')
  list_display = ('first_name', 'last_name')
  list_filter = ('age',)

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
  search_fields = ('name',)
  list_display = ('name',)
  list_filter = ('name',)
  
     