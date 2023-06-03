from django.urls import path

from employee.views import employee



urlpatterns = [
    # get all employees
    path('employees/', employee.employee_list, name='employee_list'),
    
    # Employee CRUD operations urls
    path('employee/<int:employee_id>/', employee.get_employee, name='get_employee'),
    path('employee/', employee.add_employee, name='add_employee'),
    path('employee/<int:id>/', employee.edit_employee, name='edit_employee'),
    path('employee/<int:id>/delete/', employee.delete_employee, name='delete_employee'),
]
