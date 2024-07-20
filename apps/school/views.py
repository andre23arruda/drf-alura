from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Course, Registration, Student
from .serializers import (
    CourseSerializer, RegistrationSerializer,
    StudentSerializer, StudentSerializerV2,
    CourseRegistrationSerializer, StudentRegistrationSerializer
)

class CourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['code']
    search_fields = ['code', 'description']
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
    queryset = Registration.objects.all().order_by
    serializer_class = RegistrationSerializer


class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name', 'cpf']
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    # serializer_class = StudentSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer

    @action(detail=True, methods=['get'])
    def registrations(self, request, *args, **kwargs):
        '''GET student registrations'''
        queryset = Registration.objects.filter(course=kwargs['pk'])
        serializer = StudentRegistrationSerializer(queryset, many=True)
        return Response(serializer.data)
