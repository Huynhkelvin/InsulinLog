from django.shortcuts import render, get_object_or_404
from .forms import DailyInsulinForm
from patient.models import Patient
from django.contrib.auth.models import User
from accounts.forms import ExtendedUserCreationForm
from logs.models import DailyInsulin

def detail(request):
    # log = DailyInsulin.objects.filter(patient=request.user)
    logs = DailyInsulin.objects.all()
    return render(request,'logs/detail.html',{'logs':logs})

def display(request):
    # log = DailyInsulin.objects.filter(patient=request.user)
    logs = DailyInsulin.objects.all()
    return render(request,'logs/displaylogs.html',{'logs':logs})

def insulinform(request):
    if request.method == 'POST':
        form = DailyInsulinForm(request.POST)

        if form.is_valid():
            logmodel = form.save(commit=False)
            logmodel.patient = request.user
            logmodel.diff_BSL = logmodel.curr_BSL - 130
            logmodel.correction_insulin = logmodel.diff_BSL / logmodel.patient.patient.insulin_sens
            logmodel.carb_ratio = logmodel.patient.patient.carb_ratio
            logmodel.insulin_dose = logmodel.total_carb / logmodel.carb_ratio
            logmodel.total_insulin = logmodel.correction_insulin + logmodel.insulin_dose

            logmodel.save()
            print(logmodel)

        else:
            print(request.method)
            print('invalid')
            print(form.errors)

    form = DailyInsulinForm
    context = {'patient':request.user}
    context['form'] = form
    return render(request,'logs/log.html', context)
