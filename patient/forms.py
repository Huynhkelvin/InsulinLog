from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('tar_A1c', 'insulin_sens', 'carb_ratio', 'basal','doctor',)
