from django import forms
from .models import Foodinfo, Foodtype

class FoodForm(forms.ModelForm):
    class Meta:
        model = Foodinfo
        fields = ('serving', 'carbs', 'foodtype', 'name',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].queryset = Foodinfo.objects.none()

        if 'foodtype' in self.data:
            try:
                foodtype_id = int(self.data.get('foodtype'))
                self.fields['name'].queryset = Foodinfo.objects.filter(foodtype_id=foodtype_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['name'].queryset = self.instance.foodtype.name_set.order_by('name')

class FoodInputForm(forms.ModelForm):
    class Meta:
        model = Foodinfo
        fields = ('serving', 'carbs', 'foodtype', 'name',)
        widgets = {
            'foodtype' : forms.Select(attrs={'class':'form-control',}),
            'serving' : forms.NumberInput(attrs={'class':'form-control calculate',}),
            'carbs' : forms.NumberInput(attrs={'class':'form-control',}),
            'name' : forms.TextInput(attrs={'class':'form-control',}),
        }
