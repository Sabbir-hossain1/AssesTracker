from django.db import models
from companies.models import Company
from employee.models import Employee

# Model for device
class Device(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name   


# Device Assignment
class DeviceAssignment(models.Model):
    assign_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='device_assignment_to_employee')
    devices = models.ManyToManyField(Device, related_name='device_assignment_employee')
    assign_date = models.DateField()
    return_date = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)

    # This 3 fields will track the period of assignment like "1 year 3 month and 20 days"
    assigned_for_years = models.PositiveIntegerField(default=0)
    assigned_for_months = models.PositiveIntegerField(default=0)
    assigned_for_days = models.PositiveIntegerField(default=0)

    device_condition_when_assigned = models.JSONField()
    device_condition_when_returned = models.JSONField(blank=True,null=True)

