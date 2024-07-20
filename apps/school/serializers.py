from rest_framework import serializers
from .models import Course, Registration, Student
from .validators import validate_cpf, validate_name, validate_phone


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseRegistrationSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Registration
        fields = ['student']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate(self, attrs):
        if not validate_cpf(attrs['cpf']):
            raise serializers.ValidationError({'cpf': 'O CPF deve ser válido.'})
        if not validate_phone(attrs['phone']):
            raise serializers.ValidationError({'phone': 'O telefone deve ser do formato (99) 99999-9999'})
        if not validate_name(attrs['name']):
            raise serializers.ValidationError({'name': 'O nome deve conter apenas letras'})
        return attrs


class StudentSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'phone']


class StudentRegistrationSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    def get_period(self, obj):
        return obj.get_period_display()

    class Meta:
        model = Registration
        fields = ['course', 'period']
