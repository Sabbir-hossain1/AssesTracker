from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from assets.models import Device
from assets.serializers import DeviceSerializer


@api_view(['GET'])
def device_list(request):
    """
    API view that retrieves all the device of a company from the database
    and returns them as JSON data.
    """
    devices = Device.objects.all()
    serializer = DeviceSerializer(devices, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_device(request, id):
    """
     API view that retrieves a specific device from the database
    and returns the serialized data.
    """
    device = get_object_or_404(Device, pk=id)
    serializer = DeviceSerializer(device)
    return Response(serializer.data)


@api_view(['POST'])
def add_device(request):
    """
    View for adding a new device.

    This view receives a POST request with the data to create a new device instance.
    The request body should contain the device data in JSON format.

    Returns:
        Response: HTTP response indicating the status of the operation.
    """
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def edit_device(request, id):
    """
    View for editing an existing device.

    This view receives a PUT request with the data to update a device instance.
    The request body should contain the updated device data in JSON format.
    The `id` parameter specifies the ID of the device to be edited.

    Returns:
        Response: HTTP response indicating the status of the operation.
    """
    device = get_object_or_404(Device, pk=id)
    serializer = DeviceSerializer(device, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_device(request, id):
    """
    View for deleting a device.

    This view receives a DELETE request to delete a device instance.
    The `id` parameter specifies the ID of the device to be deleted.

    Returns:
        Response: HTTP response indicating the status of the operation.
    """
    device = get_object_or_404(Device, pk=id)
    device.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

