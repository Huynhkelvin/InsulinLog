from django.db import models
from django.contrib.auth.models import User

MEAL_CHOICE = (
    ('no_meal','No Meal'),
    ('breakfast','Breakfast'),
    ('lunch','Lunch'),
    ('dinner','Dinner'),
    ('bedtime','Bedtime'),
    ('snack','Snack'),
)

class DailyInsulin(models.Model):
    meal_time = models.DateField(blank=True)
    meal = models.CharField(max_length=10, choices=MEAL_CHOICE, blank=True)
    curr_BSL = models.IntegerField(blank=True)
    diff_BSL = models.IntegerField(blank=True)
    correction_insulin = models.IntegerField(blank=True)
    total_carb = models.IntegerField(blank=True)
    carb_ratio = models.IntegerField(blank=True)
    insulin_dose = models.IntegerField(blank=True)
    total_insulin = models.IntegerField(blank=True)
    notes = models.TextField(blank=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.notes[:100]
