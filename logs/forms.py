from django import forms
from .models import DailyInsulin

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
            'meal_time': forms.DateInput(format=('%m/%d/%Y'),
                attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'meal' : forms.Select(attrs={'class':'form-control',}),
            'curr_BSL' : forms.NumberInput(attrs={'class':'form-control calculate',}),
            'insulin_dose' : forms.NumberInput(attrs={'class':'form-control',}),
            'total_carb' : forms.NumberInput(attrs={'class':'form-control',}),
            'notes' : forms.Textarea(attrs={'class':'form-control',}),
        }


    # meal_time = models.DateTimeField()
    # meal = models.CharField(max_length=10, choices=MEAL_CHOICE)
    # curr_BSL = models.IntegerField()
    # diff_BSL = models.IntegerField()
    # correction_insulin = models.IntegerField()
    # total_carb = models.IntegerField()
    # carb_ratio = models.IntegerField()
    # insulin_dose = models.IntegerField()
    # notes = models.TextField()
    # patient = models.ForeignKey(User, on_delete=models.CASCADE)
