from django.urls import path
from companies.views import companies

urlpatterns = [
     # get all companies
    path('', companies.company_list, name='company_list'),

    # Companies CRUD urls
    path('company/<int:id>/', companies.get_company, name='get_company'),
    path('company/create/', companies.create_company, name='create_company'),
    path('company/<int:id>/update/', companies.update_company, name='update_company'),
    path('company/<int:id>/delete/', companies.delete_company, name='delete_company'),
]
