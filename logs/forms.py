from django import forms
from .models import DailyInsulin
import datetime


class DailyInsulinForm(forms.ModelForm):
    curr_BSL = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class':'form-control',
        }
    ))

    class Meta:
        model = DailyInsulin
        fields = ('meal_time', 'meal', 'curr_BSL','diff_BSL','correction_insulin','total_carb','carb_ratio','insulin_dose','total_insulin', 'notes',)
        widgets = {
            'meal_time': forms.DateTimeInput(attrs={'class':'form-control','type': 'datetime-local'}),
            'meal' : forms.Select(attrs={'class':'form-control',}),
            'curr_BSL' : forms.NumberInput(attrs={'class':'form-control calculate',}),
            'insulin_dose' : forms.NumberInput(attrs={'class':'form-control',}),
            'total_carb' : forms.NumberInput(attrs={'class':'form-control',}),
            'notes' : forms.Textarea(attrs={'class':'form-control',}),
        }
