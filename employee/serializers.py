from rest_framework import serializers
from employee.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Employee model.

    This serializer is used to convert Employee instances to JSON format
    and vice versa. It includes all fields from the Employee model.
   
    """
    class Meta:
        model = Employee
        fields = '__all__'