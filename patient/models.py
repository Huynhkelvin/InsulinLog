from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tar_A1c = models.IntegerField(null=True, blank=True)
    insulin_sens = models.IntegerField(null=True, blank=True)
    carb_ratio = models.IntegerField(null=True, blank=True)
    basal = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         patient = Patient.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)
