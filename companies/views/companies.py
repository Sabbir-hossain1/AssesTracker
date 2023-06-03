from django.shortcuts import render, redirect, get_object_or_404
from companies.models import Company
from companies.forms import CompanyAdditionForm

def company_list(request):
    """
    View function that retrieves all the companies from the database
    and renders them in the 'company_list.html' template.
    """ 
    companies = Company.objects.all()
    return render(request, 'templates', {'companies': companies})

def get_company(request, id):
    """
    """
    company = get_object_or_404(Company, pk=id)
    context = {
        "company": company
    }

    return render(request, "template", context)


def create_company(request):
    """
    View function for creating a new company.

    This view function handles the HTTP POST request for creating a new company.
    It expects the request to include the form data for adding a company. If the
    form is valid, the company data is saved and the user is redirected to a success page.
    If the form is not valid, the form is rendered again with error messages.
    """
    if request.method == 'POST':
        form = CompanyAdditionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
        else:
            print("Your data is not valid")
            print("Errors: ", form.errors)            
    else:
        form = CompanyAdditionForm()

    context = {
        'form': form,
    }
    return render(request, 'template_name', context)


def update_company(request, id):
    """
    View function for updating a company.

    This view function handles the HTTP POST request for updating an existing company.
    It expects the request to include the form data for updating the company with the
    specified `id`. If the form is valid, the company data is updated and the user is
    redirected to a success page. If the form is not valid, the form is rendered again
    with error messages.
    """
    company = get_object_or_404(Company, pk=id)

    if request.method == 'POST':
        form = CompanyAdditionForm(request.POST,instance=company)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = CompanyAdditionForm(instance=company)

    context = {
        'form': form,
    }
    return render(request, 'template_name', context)

def delete_company(request, id):
    """
    View function for deleting a company.

    This view function handles the HTTP POST request for deleting a company.
    The `id` parameter specifies the ID of the company to be deleted. If the
    company is successfully deleted, the user is redirected to a success page.
    """
    company = get_object_or_404(Company, pk=id)

    if request.method == 'POST':
        company.delete()
        return redirect('success_page')

    context = {
        'company': company,
    }
    return render(request, 'template_name', context)
    
