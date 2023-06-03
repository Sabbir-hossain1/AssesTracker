from django.urls import path  

from assets.views import device, device_assignment

urlpatterns = [
    # get all devices
    path('devices/', device.device_list, name='device_list'),
    
    # Device CRUD urls
    path('device/<int:id>/',device.get_device, name="get_device"),
    path('devices/add/', device.add_device, name='add_device'),
    path('devices/<int:id>/edit/', device.edit_device, name='edit_device'),
    path('devices/<int:id>/delete/', device.delete_device, name='delete_device'),
                                
                            

    # device assignment urls    
    path('device-assignments/', device_assignment.get_device_assignments, name='get_device_assignments'),

    # Device assignment CRUD urls
    path('device-assignment/<int:id>/', device_assignment.get_device_assignment, name='get_device_assignment'),
    path('device-assignments/create/', device_assignment.create_device_assignment, name='create_device_assignment'),
    path('device-assignments/<int:id>/update/', device_assignment.update_device_assignment, name='update_device_assignment'),
    path('device-assignments/<int:id>/delete/', device_assignment.delete_device_assignment, name='delete_device_assignment'),                               
    ]                        

