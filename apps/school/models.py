from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=11)
    birth_date = models.DateField()
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_CHOICES = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100, blank=False)
    level = models.CharField(max_length=2, blank=False, null=False, choices=LEVEL_CHOICES, default='B')

    def __str__(self):
        return self.code


class Registration(models.Model):
    PERIOD_CHOICES = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    period = models.CharField(max_length=2, choices=PERIOD_CHOICES, default='M', null=False, blank=False)

    def __str__(self):
        return self.student.name + ' - ' + self.course.code
