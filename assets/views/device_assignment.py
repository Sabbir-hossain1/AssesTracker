from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from assets.models import DeviceAssignment
from assets.serializers import DeviceAssignmentSerializer


@api_view(['GET'])
def get_device_assignments(request):
    """
    API view that retrieves all device assignments from the database
    and returns the serialized data.
    """

    device_assignments = DeviceAssignment.objects.all()
    serializer = DeviceAssignmentSerializer(device_assignments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_device_assignment(request, id):
    """
    API view that retrieves a specific device assignment from the database
    and returns the serialized data.
    """

    try:
        assignment = DeviceAssignment.objects.get(id=id)
    except DeviceAssignment.DoesNotExist:
        return Response({'error': 'Device assignment not found'}, status=404)

    serializer = DeviceAssignmentSerializer(assignment)
    return Response(serializer.data)



@api_view(['POST'])
def create_device_assignment(request):
    """
    View for creating a new device assignment.

    This view receives a POST request with the data to create a new device assignment.
    The request body should contain the device assignment data in JSON format.

    """
    serializer = DeviceAssignmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_device_assignment(request, id):
    """
    View for updating an existing device assignment.

    This view receives a PUT request with the data to update a device assignment.
    The request body should contain the updated device assignment data in JSON format.
    The `id` parameter specifies the ID of the device assignment to be updated.
   
    """
    device_assignment = get_object_or_404(DeviceAssignment, pk=id)
    serializer = DeviceAssignmentSerializer(device_assignment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_device_assignment(request, id):
    """
    View for deleting a device assignment.

    This view receives a DELETE request to delete a device assignment.
    The `id` parameter specifies the ID of the device assignment to be deleted.

    """
    device_assignment = get_object_or_404(DeviceAssignment, pk=id)
    device_assignment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def device_assignment_detail(request, id):
    """
    View for retrieving details of a device assignment(when check in/out and conditions).

    This view receives a GET request to retrieve the details of a specific device assignment.
    The `id` parameter specifies the ID of the device assignment.
    """
    device_assignment = get_object_or_404(DeviceAssignment, pk=id)
    serializer = DeviceAssignmentSerializer(device_assignment)
    return Response(serializer.data)
