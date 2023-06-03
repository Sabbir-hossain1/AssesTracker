from django import forms

from companies.models import Company


class CompanyAdditionForm(forms.ModelForm):
    """
    A form for adding a new company.

    This form is used to collect and validate data for creating a new company
    object. It is based on the Company model and includes all fields defined
    in the model.

    Attributes:
        Meta (class): A inner class that provides metadata for the form.
            - model (Model): The model class associated with the form.
            - fields (list or '__all__'): The fields to include in the form.
    """

    class Meta:
        model = Company
        fields = '__all__'
