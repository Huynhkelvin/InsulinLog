from django.shortcuts import render, get_object_or_404
from .forms import DailyInsulinForm
from patient.models import Patient
from django.contrib.auth.models import User
from accounts.forms import ExtendedUserCreationForm


    # form = ExtendedUserCreationForm(request.POST)
    # patient_form = PatientForm(request.POST)
    #
    # if form.is_valid() and patient_form.is_valid():
    #     user = form.save()
    #     patient = patient_form.save(commit=False)
    #     patient.user = user
    #     patient.save()

def insulinform(request):
    if request.method == 'POST':
        form = DailyInsulinForm(request.POST)

        if form.is_valid():
            logmodel = form.save(commit=False)
            logmodel.patient = request.user
            print(logmodel.patient)
            logmodel.diff_BSL = logmodel.curr_BSL-130
            logmodel.carb_ratio = logmodel.patient.patient.carb_ratio
            logmodel.correction_insulin = logmodel.diff_BSL / logmodel.patient.patient.insulin_sens
            logmodel.insulin_dose = logmodel.total_carb / logmodel.carb_ratio
            logmodel.total_insulin = logmodel.insulin_dose + logmodel.correction_insulin
            logmodel.save()

        else:
            print('invalid')
            print(form.errors)

    form = DailyInsulinForm
    context = {'patient':request.user}
    context['form'] = form
    return render(request,'logs/log.html', context)
