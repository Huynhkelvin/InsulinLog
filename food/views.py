from django.shortcuts import render
from .models import Foodinfo
from .forms import FoodForm, FoodInputForm

def calculatecarb(request):
    qs = Foodinfo.objects.all()
    food_contains_query = request.GET.get('food_contains')
    food_exact_query = request.GET.get('food_exact')
    if food_contains_query != '' and food_exact_query is not None:
        qs = qs.filter(name__icontains=food_contains_query)
    context = {
        'queryset': qs
    }
    return render(request, 'food/carbcount.html', context)

def addfood(request):
    if request.method =='POST':
        form = FoodInputForm(request.POST)
        if form.is_valid():
            foodmodel = form.save()
        else:
            print('invalid')
            print(form.errors)
    form = FoodInputForm()
    # context = {'food': form}
    return render(request,'food/addfood.html',{'form':form})
