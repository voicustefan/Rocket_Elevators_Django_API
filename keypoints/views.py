from rest_framework import viewsets
from .serializers import EmployeesSerializer
from .models import Employees

class EmployeeViewSet(viewsets.ModelViewSet) :
    queryset = Employees.objects.all().order_by('id')
    serializer_class = EmployeesSerializer
