from rest_framework import generics
from .models import Employee, Department, Appraisal
from .serializers import AppraisalSerializer, DepartmentSerializer, EmployeeSerializer
# Create your views here.

class EmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentAPIView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class AppraisalAPIView(generics.ListCreateAPIView):
    queryset = Appraisal.objects.all()
    serializer_class = AppraisalSerializer