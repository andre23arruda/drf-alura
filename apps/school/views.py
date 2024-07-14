from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Course, Registration, Student
from .serializers import (
    CourseSerializer, RegistrationSerializer, StudentSerializer,
    CourseRegistrationSerializer, StudentRegistrationSerializer
)

class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['get'])
    def registrations(self,  request, *args, **kwargs):
        '''GET course registrations'''
        queryset = Registration.objects.filter(course=kwargs['pk'])
        serializer = CourseRegistrationSerializer(queryset, many=True)
        return Response(serializer.data)


class RegistrationViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['get'])
    def registrations(self, request, *args, **kwargs):
        '''GET student registrations'''
        queryset = Registration.objects.filter(course=kwargs['pk'])
        serializer = StudentRegistrationSerializer(queryset, many=True)
        return Response(serializer.data)
