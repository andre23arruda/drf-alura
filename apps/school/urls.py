from django.urls import path, include
from rest_framework import routers
from .views import CourseViewSet, RegistrationViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet, basename='Courses')
router.register('registrations', RegistrationViewSet, basename='Registrations')
router.register('students', StudentViewSet, basename='Students')

urlpatterns = [
    path('', include(router.urls)),
]