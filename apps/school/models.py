from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

CPF_REGEX_1 = r'^\d{11}$'
CPF_REGEX_2 = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
NAME_REGEX = r"^[A-Z a-z]+$"
PHONE_REGEX = r'^\(?(\d{2})\)?\s?(\d{4,5})[- ](\d{4})$'

class Student(models.Model):
    name = models.CharField(max_length=100)#, validators=[RegexValidator(NAME_REGEX)])
    email = models.EmailField()
    cpf = models.CharField(max_length=14, unique=True)#, validators=[RegexValidator(CPF_REGEX)])
    birth_date = models.DateField()
    phone = models.CharField(max_length=16)#, validators=[RegexValidator(PHONE_REGEX)])

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_CHOICES = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    code = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(3)])
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
