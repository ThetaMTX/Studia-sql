from django import forms
from .models import Patient, Examination

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'pesel']  # other fields here pls
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

class ExaminationForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = ['description', 'images']
