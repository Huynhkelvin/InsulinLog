from django.db import models

class Foodtype(models.Model):
    type =  models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Foodinfo(models.Model):
    serving = models.IntegerField(null=True, blank=True)
    carbs = models.IntegerField(null=True, blank=True)
    foodtype = models.ForeignKey(Foodtype, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
