from django.db import models
from companies.models import Company


# Model for employee
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=100) # it can be another model which can connect with foreign key
    designation = models.CharField(max_length=100)
    joining_dae = models.DateField()    
    phone_number = models.CharField(max_length=20)
    emergency_phone_number = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='employee_img/')
    branch_name = models.CharField(max_length=50)  # it can be another model which can connect with foreign key
    bank_account_name = models.CharField(max_length=30)
    bank_account_no = models.CharField(max_length=20)
    address = models.TextField()

    # relation with company
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employee_company')     

    def __str__(self):
        return self.first_name