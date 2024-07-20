from django.contrib import admin
from .models import Course, Registration, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'description', 'level']
    ordering = ['code']


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'period']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'cpf', 'birth_date', 'phone']
    ordering = ['name']
