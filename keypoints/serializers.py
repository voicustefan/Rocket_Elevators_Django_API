# serializers.py
from rest_framework import serializers

from .models import Employees

class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = ('id', 'title', 'firstname', 'lastname', 'email', 'password', 'created_at', 'updated_at', 'facial_keypoints' )