from django.db import models

# Model for companies
class Company(models.Model):
    name = models.CharField(max_length=100)
    slogan = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to='company_logo/')
    establish_date = models.DateField()
    website = models.URLField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=400)

    def __str__(self):
        return self.name
