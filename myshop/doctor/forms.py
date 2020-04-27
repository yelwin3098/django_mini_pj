from django import forms
from .models import Category,Doctor

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['category','name','quali','duty']