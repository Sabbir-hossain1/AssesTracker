from rest_framework import serializers
from assets.models import Device, DeviceAssignment

class DeviceSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Device model.

    This serializer is used to convert Device instances to JSON format
    and vice versa. It includes all fields from the Device model.

    """
    class Meta:
        model = Device
        fields = '__all__'


class DeviceAssignmentSerializer(serializers.ModelSerializer):
    """
    Serializer class for the DeviceAssignment model.

    This serializer is used to convert DeviceAssignment instances to JSON format
    and vice versa. It includes all fields from the DeviceAssignment model.

    """
    class Meta:
        model = DeviceAssignment
        fields = '__all__'