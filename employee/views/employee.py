from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from employee.models import Employee
from employee.serializers import EmployeeSerializer


@api_view(['GET'])
def employee_list(request):
    """
    API view that retrieves all the employees of a company from the database
    and returns them as JSON data.
    """

    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_employee(request, employee_id):
    """
    API view that retrieves a specific employee from the database
    and returns the serialized data.
    """

    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=404)

    serializer = EmployeeSerializer(employee)
    return Response(serializer.data)


@api_view(['POST'])
def add_employee(request):
    """
    View for adding a new employee.

    This view receives a POST request with the data to create a new employee instance.
    The request body should contain the employee data in JSON format.

    return: Response: HTTP response indicating the status of the operation.
    """
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_employee(request, id):
    """
    View for editing an existing employee.

    This view receives a PUT request with the data to update an employee instance.
    The request body should contain the updated employee data in JSON format.
    The `id` parameter specifies the ID of the employee to be edited.

    return: Response: HTTP response indicating the status of the operation.
    """
    employee = get_object_or_404(Employee, pk=id)
    serializer = EmployeeSerializer(employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_employee(request, id):
    """
    View for deleting an employee.

    This view receives a DELETE request to delete an employee instance.
    The `id` parameter specifies the ID of the employee to be deleted.

    return Response: HTTP response indicating the status of the operation.
    """
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
